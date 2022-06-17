from zipfile import ZipFile


def create_backup():
    with ZipFile('src/system/backup/backup.zip', 'w') as backup_zip:
        backup_zip.write('src/database/database.db')
        backup_zip.write('src/system/logging/log.log')


def restore_backup():
    with ZipFile('src/system/backup/backup.zip', 'r') as backup_zip:
        backup_zip.extractall()
