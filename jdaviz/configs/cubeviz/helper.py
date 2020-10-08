from jdaviz.core.helpers import ConfigHelper
from jdaviz.configs.default.plugins.line_lists.line_list_mixin import LineListMixin
from jdaviz.configs.specviz import SpecViz

class CubeViz(ConfigHelper, LineListMixin):
    """CubeViz Helper class"""
    _default_configuration = 'cubeviz'

    @property
    def specviz(self):
        """
        A specviz helper for the app this helper wraps
        """
        if not hasattr(self, '_specviz'):
            self._specviz = SpecViz(app=self.app)
        return self._specviz
