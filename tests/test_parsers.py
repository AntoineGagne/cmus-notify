from cmus_notify.parsers import parse_status_information
from cmus_notify.types import StatusInformation


def test_that_given_incomplete_informations_when_parse_status_information_then_it_parse_a_status_information():
    incomplete_information = "status playing file ~/Music/Cave Story/Cave Story/Cave Story OST - 01_41 - Access.m4a artist Daisuke Amaya album Cave Story OST discnumber 1 title Access date 2004 duration 45"

    status_information = parse_status_information(incomplete_information)

    assert status_information.__dict__ == {
        "albumartist": "N/A",
        "artist": "Daisuke Amaya",
        "duration": "00:45",
        "date": "2004",
        "file": "~/Music/Cave Story/Cave Story/Cave Story OST - 01_41 - Access.m4a",
        "title": "Access",
        "discnumber": 1,
        "status": "Playing",
        "album": "Cave Story OST",
        "tracknumber": "N/A",
    }


def test_that_given_empty_informations_when_parse_status_information_then_it_returns_empty_status_information():
    status_information = parse_status_information("")
    assert status_information.__dict__ == StatusInformation().__dict__


def test_that_given_complete_informations_when_parse_status_information_then_it_parse_a_complete_status_information():
    incomplete_information = "status playing file ~/Music/Cave Story/Cave Story/Cave Story OST - 01_41 - Access.m4a artist Daisuke Amaya album Cave Story OST discnumber 1 title Access date 2004 tracknumber 1 duration 45 albumartist Daisuke Amaya"

    status_information = parse_status_information(incomplete_information)

    assert status_information.__dict__ == {
        "albumartist": "Daisuke Amaya",
        "artist": "Daisuke Amaya",
        "duration": "00:45",
        "date": "2004",
        "file": "~/Music/Cave Story/Cave Story/Cave Story OST - 01_41 - Access.m4a",
        "title": "Access",
        "discnumber": 1,
        "status": "Playing",
        "album": "Cave Story OST",
        "tracknumber": 1,
    }
