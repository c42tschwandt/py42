from py42.sdk.queries.query_filter import (
    QueryFilterStringField,
    create_filter_group,
    create_query_filter,
    QueryFilterTimestampField,
)


def create_contains_filter_group(term, value):
    filter_list = [create_query_filter(term, u"CONTAINS", value)]
    return create_filter_group(filter_list, u"AND")


def create_not_contains_filter_group(term, value):
    filter_list = [create_query_filter(term, u"DOES_NOT_CONTAIN", value)]
    return create_filter_group(filter_list, u"AND")


class AlertQueryFilterStringField(QueryFilterStringField):
    @classmethod
    def contains(cls, value):
        return create_contains_filter_group(cls._term, value)

    @classmethod
    def not_contains(cls, value):
        return create_not_contains_filter_group(cls._term, value)


class DateObserved(QueryFilterTimestampField):
    """Class that filters alerts based on the timestamp the alert was triggered."""

    _term = u"CreatedAt"


class Actor(AlertQueryFilterStringField):
    """Class that filters alerts based on the username that originated the event(s) that
    triggered the alert."""

    _term = u"actor"


class RuleName(AlertQueryFilterStringField):
    """Class that filters alerts based on rule name."""

    _term = u"name"


class Description(AlertQueryFilterStringField):
    """Class that filters alerts based on rule description text."""

    _term = u"description"


class Severity(QueryFilterStringField):
    """Class that filters alerts based on severity.

    Available options are:
        - :attr:`Severity.HIGH`
        - :attr:`Severity.MEDIUM`
        - :attr:`Severity.LOW`
    """

    _term = u"severity"

    HIGH = u"HIGH"
    MEDIUM = u"MEDIUM"
    LOW = u"LOW"


class AlertState(QueryFilterStringField):
    """Class that filters alerts based on alert state.

    Available options are:
        - :attr:`AlertState.OPEN`
        - :attr:`AlertState.DISMISSED`
    """

    _term = u"state"

    OPEN = u"OPEN"
    DISMISSED = u"RESOLVED"
