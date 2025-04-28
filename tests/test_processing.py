import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(my_lists: list[dict], state: str, expected: list[dict]) -> None:
    assert filter_by_state(my_lists, state) == expected


@pytest.mark.parametrize("list_dicts", [[{"id": 594226727, "date": "2018-09-12T21:27:25.241689"}], [{}]])
def test_filter_by_state_invalid(list_dicts: list[dict]) -> None:
    assert filter_by_state(list_dicts) == []


@pytest.mark.parametrize(
    "sort_param, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(dates: list[dict], sort_param: bool, expected: list[dict]) -> None:
    assert sort_by_date(dates, sort_param) == expected


def test_sort_by_date_same_dates() -> None:
    assert sort_by_date(
        [
            {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_invalid_dates(dates: list[dict]) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "209-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-13-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-112T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-02-31T02:08:58.425572"},
            ]
        )
        == []
    )
