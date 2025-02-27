
from src import app, db
from src.methods_for_tests import init_test_db, clear_unittest_records, clear_master_data, is_alias_present, init_db_create

def test_recommendation_anak_soleh_pelajar():
    init_db_create()
    init_test_db()

    body = {
        "age": 15,
        "salary": 0,
        "job": 0, # pelajar
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

def test_recommendation_pemula_mandiri_mahasiswa():
    init_db_create()
    init_test_db()

    body = {
        "age": 17,
        "salary": 0,
        "job": 1, # mahasiswa
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Pemula Mandiri"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert is_alias_present(response.get_json()['products'], "tabungan-wadiah")

def test_recommendation_pemula_mandiri_pelajar():
    init_db_create()
    init_test_db()

    body = {
        "age": 17,
        "salary": 1,
        "job": 0, # pelajar
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Pemula Mandiri"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert is_alias_present(response.get_json()['products'], "tabungan-wadiah")

def test_recommendation_pemula_mandiri_pegawai():
    init_db_create()
    init_test_db()

    body = {
        "age": 17,
        "salary": 1,
        "job": 2, # pegawai
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Pemula Mandiri"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert is_alias_present(response.get_json()['products'], "tabungan-wadiah")

def test_recommendation_profesional_berkah_mahasiswa():
    init_db_create()
    init_test_db()

    body = {
        "age": 17,
        "salary": 2,
        "job": 1, # mahasiswa
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Profesional Berkah"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert is_alias_present(response.get_json()['products'], "tabungan-wadiah")

def test_recommendation_profesional_berkah_pegawai_5juta():
    init_db_create()
    init_test_db()

    body = {
        "age": 25,
        "salary": 2,
        "job": 2, # pegawai
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Profesional Berkah"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 6

def test_recommendation_profesional_berkah_pegawai_10juta():
    init_db_create()
    init_test_db()

    body = {
        "age": 25,
        "salary": 3,
        "job": 2, # pegawai
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Profesional Berkah"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 6

def test_recommendation_syariah_salary_club():
    init_db_create()
    init_test_db()

    body = {
        "age": 25,
        "salary": 3,
        "job": 3, # ASN
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Syariah Salary Club"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 3

def test_recommendation_wirausahawan_sukses_10jt():
    init_db_create()
    init_test_db()

    body = {
        "age": 25,
        "salary": 3,
        "job": 4, # wirus
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Wirausahawan Sukses"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 3

def test_recommendation_wirausahawan_sukses_15jt():
    init_db_create()
    init_test_db()

    body = {
        "age": 25,
        "salary": 4,
        "job": 4, # wirus
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Wirausahawan Sukses"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 3

def test_recommendation_pilar_keluarga_15jt():
    init_db_create()
    init_test_db()

    body = {
        "age": 36,
        "salary": 4,
        "job": 2, # pegawai
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Pilar Keluarga"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 4

def test_recommendation_investor_wirus():
    init_db_create()
    init_test_db()

    body = {
        "age": 36,
        "salary": 5,
        "job": 4, # wirus
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Investor Sejati"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 3

def test_recommendation_investor_pegawai():
    init_db_create()
    init_test_db()

    body = {
        "age": 36,
        "salary": 5,
        "job": 2, # pegawai
        "gender": 0,
        "province": "Jawa Barat"
    }

    client = app.test_client()
    endpoint = "/recommendations"

    response = client.post(endpoint, json=body)
    print(response.get_json())

    clear_unittest_records(response.get_json()['user_input_id'])

    assert response.status_code == 201
    assert response.get_json()['segmentation']['name'] == "Investor Sejati"
    assert is_alias_present(response.get_json()['products'], "deposito")
    assert len(response.get_json()["products"]) == 4
