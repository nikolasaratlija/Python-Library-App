from zipfile import ZipFile
from os.path import exists
from src.system.logging.logger import log


def create_backup():
    try:
        with ZipFile('src/system/backup/backup.zip', 'w') as backup_zip:
            backup_zip.write('src/database/ENCRYPTED-database.db')
            backup_zip.write('src/system/logging/ENCRYPTED-log.log')
            log('Restored from backup', 'System has been successfully restored from backup.')
            return True, 'Backup has successfully been created'
    except FileNotFoundError:
        log('Create backup error',
            'The required files are not present in the system. Cannot continue with the operation')
        return False, 'The required files are not present in the system. Cannot continue with the operation'


def restore_backup():
    if not exists('src/system/backup/backup.zip'):
        log('Restore backup error', 'No existing backup has been found. Try making a backup first.')
        return False, 'No existing backup has been found. Try making a backup first.'

    with ZipFile('src/system/backup/backup.zip', 'r') as backup_zip:
        backup_zip.extractall()
        log('Restored from backup', 'System has been successfully restored from backup.')
        return True, 'System has been successfully restored from backup.'
