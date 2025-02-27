
from src import app, db
from src.methods_for_tests import init_test_db, clear_unittest_records, clear_master_data, is_alias_present, init_db_create

def test_recommendation_anak_soleh_pelajar():
    init_db_create()
    init_test_db()

    body = {
        "age": 15,
        "salary": 0,
        "job": 0,
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Anak Sholeh"
    assert len(response.get_json()['products']) == 2
    assert is_alias_present(response.get_json()['products'], "bsi-simpel")
    assert is_alias_present(response.get_json()['products'], "ziswaf")


