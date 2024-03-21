from mock_db import fake_generator,  ingest_fake_table


if __name__ == '__main__':
    fake_generator.generate_fake_information()
    ingest_fake_table.ingest_fake_tables()