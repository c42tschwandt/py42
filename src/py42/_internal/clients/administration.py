from py42._internal.base_classes import BaseAuthorityClient


class AdministrationClient(BaseAuthorityClient):
    def get_diagnostics(self, include_volumes=None, **kwargs):
        uri = u"/api/Diagnostic"
        params = {u"incVolumes": include_volumes}
        return self._default_session.get(uri, params=params, **kwargs)

    def get_alert_log(self, status=None, alert_type=None, page_num=None, page_size=None, **kwargs):
        uri = u"/api/AlertLog"
        params = {u"status": status, u"type": alert_type, u"pgNum": page_num, u"pgSize": page_size}
        return self._default_session.get(uri, params=params, **kwargs)