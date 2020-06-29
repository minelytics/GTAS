from gtas.parsers.paxlst.segment import att
from gtas.parsers.paxlst.segment import bgm
from gtas.parsers.paxlst.segment import cnt
from gtas.parsers.paxlst.segment import com
from gtas.parsers.paxlst.segment import doc
from gtas.parsers.paxlst.segment import dtm
from gtas.parsers.paxlst.segment import loc
from gtas.parsers.paxlst.segment import nad
from gtas.parsers.paxlst.segment import nat
from gtas.parsers.paxlst.segment import rff
from gtas.parsers.paxlst.segment import tdt


class PaxlstParser:
    def get_segment(self, val):
        switch = {
            "ATT": att,
            "BGM": bgm,
            "CNT": cnt,
            "COM": com,
            "DOC": doc,
            "DTM": dtm,
            "LOC": loc,
            "NAD": nad,
            "NAT": nat,
            "RFF": rff,
            "TDT": tdt
        }
        return switch.get(val, "Paxlst Parser Undefined segment: " + val)
