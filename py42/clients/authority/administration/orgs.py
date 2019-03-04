from py42.clients.authority.authority_base import AuthorityTargetedClient
import json


class OrgClient(AuthorityTargetedClient):

    def create_org(self, org_name, org_ext_ref=None, notes=None,
                   parent_org_uid=None, classification=None, **kwargs):
        uri = "/api/Org/"
        data = {"orgName": org_name, "orgExtRef": org_ext_ref, "notes": notes, "parentOrgUid": parent_org_uid,
                "classification": classification}
        return self.post(uri, data=json.dumps(data), **kwargs)

    def get_org_by_uid(self, org_uid, **kwargs):
        uri = "/api/Org/{}?idType=orgUid".format(org_uid)
        return self.get(uri, **kwargs)

    def get_orgs(self, page_num=None, page_size=None, **kwargs):
        uri = "/api/Org"
        params = {"pgNum": page_num, "pgSize": page_size}

        return self.get(uri, params=params, **kwargs)

    def get_current_user_org(self, **kwargs):
        uri = "/api/Org/my"
        return self.get(uri, **kwargs)
