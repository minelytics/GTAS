import json


def load_schema(schema_file, interchange_header_file="unb.json",
                interchange_trailer_file="unz.json", service_string_advice_file="una.json", verbose=False):
    # combine UNB definition with the supplied CUSCAR message definition
    with open(interchange_header_file) as json_file:
        cuscar_unb_schema = json.load(json_file)

    with open(interchange_trailer_file) as json_file:
        cuscar_unz_schema = json.load(json_file)

    with open(service_string_advice_file) as json_file:
        cuscar_una_schema = json.load(json_file)

    with open(schema_file) as json_file:
        cuscar_schema = json.load(json_file)
        if verbose:
            print(cuscar_schema)

    json_schema = [cuscar_una_schema, cuscar_unb_schema, cuscar_unz_schema]
    json_schema.extend(cuscar_schema)

    return json_schema


class SchemaIterator():
    def __init__(self, parent):
        self._list_position = 0
        self._loop_count = 1
        self._parent = parent

    def _list(self):
        pass

    def _has_next_siblings(self):
        return self._list_position < len(self._list()) - 1

    def _has_next_optional_loop(self, follow_loops=True):
        if follow_loops:
            cardinality = int(self.current_segment()['cardinality'])
            result = self._loop_count < cardinality
            # print(f"Current tag {self.current_segment_tag()} cardinality {self.current_segment()['cardinality']}
            # loop_count {self._loop_count} result {result}")
            return result
        else:
            return False

    def no_more_loops_for_current_tag(self):
        # print(f'No more loops for {self.position()}')
        cardinality = int(self.current_segment()['cardinality'])
        self._loop_count = cardinality

    def _has_parent_next(self):
        return self._parent is not None and self._parent.has_next()

    def has_next(self, follow_loops=True):
        return self._has_next_siblings() or self._has_next_optional_loop(follow_loops) or self._has_parent_next()

    def next(self, follow_loops=True):
        if not self.has_next(follow_loops):
            raise Exception('No more segments')

        if not self._has_next_optional_loop(follow_loops):
            if self._has_next_siblings():
                self._list_position += 1
                self._loop_count = 0
            else:
                return self._parent.next(follow_loops=follow_loops)

        self._loop_count += 1
        if self.current_segment()['element_type'] == 'Group':
            grp_iter = GroupIterator(self.current_segment(), self)
            return grp_iter
        else:
            return self

    def current_segment(self):
        return self._list()[self._list_position]

    def current_segment_tag(self):
        return self.current_segment()['code']

    def position(self):
        return {'code': self.position_code(), 'desc': self.position_description()}

    def position_code(self):
        result = self.current_segment_tag()
        if self._parent is not None:
            result += '>' + self._parent.position_code()
        return result

    def position_description(self):
        result = self.current_segment()['desc']
        if self._parent is not None:
            result += '\n  ' + self._parent.position_description()
        return result


class RootListIterator(SchemaIterator):
    def __init__(self, schema):
        super().__init__(None)
        self._schema = schema

    def _list(self):
        return self._schema

    def has_just_entered_group(self):
        return False


class GroupIterator(SchemaIterator):
    def __init__(self, group, parent):
        super().__init__(parent)
        self._group = group

    def _list(self):
        return self._group['sections']

    def has_just_entered_group(self):
        return self._list_position == 0

    def group_tag(self):
        return self._group['code']

    def skip(self):
        self._parent.no_more_loops_for_current_tag()
        return self._parent.next()


class GroupSkip:
    def __init__(self):
        self._already_visited_groups = []

    def already_visited(self, iterator):
        if iterator.has_just_entered_group():
            current_group = iterator.group_tag()
            if current_group in self._already_visited_groups:
                return True
            else:
                self._already_visited_groups.append(current_group)
        return False


class SchemaTraverser:

    def __init__(self, schema):
        self._iterator = RootListIterator(schema)

    def find_segment_forward(self, segment_code):
        group_skip = GroupSkip()

        while self._iterator is not None:
            # print(f'Looking for {segment_code} current position {self._iterator.position()}' )

            result = None
            position = None

            if group_skip.already_visited(self._iterator):
                self._iterator = self._iterator.skip()
            else:
                if self._iterator.current_segment_tag() == segment_code:
                    result = self._iterator.current_segment()
                    position = self._iterator.position()
                else:
                    # no need to check the current tag again as it didn't match
                    self._iterator.no_more_loops_for_current_tag()

                if self._iterator.has_next():
                    self._iterator = self._iterator.next()
                else:
                    self._iterator = None

                if result is not None:
                    # print(f"Result found at schema position {position}")
                    return result, position

        raise Exception(f"Segment not found {segment_code}")

    # Returns a generator that can walk over all segments once
    def segment_generator(self, follow_loops=False):
        yield self._iterator.current_segment()
        while True:
            self._iterator = self._iterator.next(follow_loops)
            yield self._iterator.current_segment()
            if not self._iterator.has_next(follow_loops):
                break
