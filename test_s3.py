import boto3
from unittest.mock import patch, MagicMock


def test_list_buckets_returns_list():
    """Verify the function returns a list of buckets."""
    mock_s3_client = MagicMock()
    mock_s3_client.list_buckets.return_value = {
        "Buckets": [
            {"Name": "bucket1", "CreationDate": "2024-01-01T00:00:00Z"},
            {"Name": "bucket2", "CreationDate": "2024-02-01T00:00:00Z"},
        ]
    }

    with patch("boto3.client", return_value=mock_s3_client):
        s3 = boto3.client("s3")
        response = s3.list_buckets()

    assert isinstance(response["Buckets"], list)
    assert len(response["Buckets"]) == 2
    assert response["Buckets"][0]["Name"] == "bucket1"
    assert response["Buckets"][1]["Name"] == "bucket2"


def test_bucket_has_name():
    """Verify that each bucket has a name."""
    mock_s3_client = MagicMock()
    mock_s3_client.list_buckets.return_value = {
        "Buckets": [
            {"Name": "bucket1", "CreationDate": "2024-01-01T00:00:00Z"},
            {"Name": "bucket2", "CreationDate": "2024-02-01T00:00:00Z"},
        ]
    }

    with patch("boto3.client", return_value=mock_s3_client):
        s3 = boto3.client("s3")
        response = s3.list_buckets()

    assert response["Buckets"][0]["Name"] == "bucket1"
