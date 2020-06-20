from pydifact.message import Message
message = Message.from_file("../input/20200506 0432_API_50157_YY123_IAD_BRU_20200506 1700.txt")

for segment in message.segments:
    print('Segment tag: {}, content: {}'.format(
        segment.tag, segment.elements))
