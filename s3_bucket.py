#* Menggunakan AWS SDK (Boto3) untuk Mengelola S3
#! Mengunggah file ke bucket S3.
import boto3

def upload_to_s3(bucket_name, file_path, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Failed to upload file: {e}")

# Contoh penggunaan
upload_to_s3("my-bucket", "test.txt")