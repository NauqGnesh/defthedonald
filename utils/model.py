from typing import Optional
import boto3
import os


class Model:
	DESTINATION_PATH = "/tmp/"
	DIRECTORY_IN_BUCKET = "models"
	BUCKET = "defthedonald"
	is_fetched = False
	has_begun_fetch = False

	@classmethod
	def _download_s3_dir(cls, bucket_name: str, remote_dir_name: str) -> None:
		app_root = os.getcwd()
		s3_resource = boto3.resource('s3')
		bucket = s3_resource.Bucket(bucket_name)
		for obj in bucket.objects.filter(Prefix=remote_dir_name):
			file_destination_path = app_root + cls.DESTINATION_PATH + obj.key
			file_destination_dir = os.path.dirname(file_destination_path)
			if not os.path.exists(file_destination_dir):
				os.makedirs(file_destination_dir)
				print(f"Created directory {file_destination_dir}")
			bucket.download_file(obj.key, file_destination_path)
			print(f"Downloaded {obj.key} to {file_destination_path}")

	@classmethod
	def get_path(cls) -> Optional[str]:
		if cls.is_fetched:
			return os.getcwd() + cls.DESTINATION_PATH + cls.DIRECTORY_IN_BUCKET
		elif not cls.has_begun_fetch:
			cls.fetch()
		return None

	@classmethod
	def fetch(cls) -> None:
		print("Fetching...")
		cls._download_s3_dir(cls.BUCKET, cls.DIRECTORY_IN_BUCKET + "/")
		cls.is_fetched = True
		print("Fetch complete. Ready for requests")