import csv
from StringIO import StringIO
from pkg_resources import resource_string


class LevelDustCosts:
    def __init__(self):
        self._stats = self._load_stats()

    def _load_stats(self):
        contents = resource_string('pogoiv', 'data/level_dust_costs.tsv')
        f = StringIO(contents)
        reader = csv.reader(f, delimiter='\t')

        stats = {}
        for index, row in enumerate(reader):
            if index == 0:
                continue
            dust_cost, level = row
            stats[int(dust_cost)] = int(level)
        return stats

    def get_level_range(self, dust_cost):
        """
        :param dust_cost: Integer representing the upgrade cost in dust for the pokemon.
        :return: (integer, integer) representing the lowest and high possible levels for the pokemon.
        """
        min_level = self._stats[dust_cost]
        return (float(min_level), min_level + 1.5)
