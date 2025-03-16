import unittest
from unittest.mock import patch, MagicMock
from src.core.database import update_file_database, get_all_files, insert_file_data, delete_file, check_file_exists


class TestDatabase(unittest.TestCase):

    @patch('src.core.database.scan_directory')
    @patch('src.core.database.get_all_files')
    @patch('src.core.database.get_metadata')
    @patch('src.core.database.calculate_size')
    @patch('src.core.database.get_file_hash')
    @patch('src.core.database.insert_file_data')
    @patch('src.core.database.delete_file')

    def test_update_file_database(self, mock_delete_file, mock_insert_file_data,
                                  mock_get_file_hash, mock_get_metadata, mock_calculate_size,
                                  mock_get_all_files, mock_scan_directory):
        # Setup mock return values
        mock_scan_directory.return_value = ['file1.mp4', 'file2.mp4']
        mock_get_all_files.return_value = [('file3.mp4',), ('file4.mp4',)]
        mock_get_metadata.return_value = ("title", "creator")
        mock_calculate_size.return_value = "1GB"
        mock_get_file_hash.return_value = "file_hash"

        # Call the function
        update_file_database('mock_directory')

        # Assert insert_file_data called for new files
        mock_insert_file_data.assert_any_call('file1.mp4', unittest.mock.ANY, "file_hash", "title", "creator")
        mock_insert_file_data.assert_any_call('file2.mp4', unittest.mock.ANY, "file_hash", "title", "creator")

        # Assert delete_file called for missing files
        mock_delete_file.assert_any_call('file3.mp4')
        mock_delete_file.assert_any_call('file4.mp4')

    @patch('src.core.database.connect_db')
    def test_get_all_files(self, mock_connect_db):
        # Setup mock
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('file1.mp4',), ('file2.mp4',)]
        mock_connect_db.return_value = (MagicMock(), mock_cursor)

        # Call the function
        result = get_all_files()

        # Assert the result
        self.assertEqual(result, [('file1.mp4',), ('file2.mp4',)])

    @patch('src.core.database.connect_db')
    def test_insert_file_data(self, mock_connect_db):
        # Setup mock
        mock_cursor = MagicMock()
        mock_connect_db.return_value = (MagicMock(), mock_cursor)

        # Call the function
        insert_file_data('file.mp4', '1GB', 'hash', 'creator', 'title')

        # Assert execute called
        mock_cursor.execute.assert_called_once()

    @patch('src.core.database.connect_db')
    def test_delete_file(self, mock_connect_db):
        # Setup mock
        mock_cursor = MagicMock()
        mock_connect_db.return_value = (MagicMock(), mock_cursor)

        # Call the function
        delete_file('hash')

        # Assert execute called
        mock_cursor.execute.assert_called_once()

    @patch('src.core.database.connect_db')
    def test_check_file_exists(self, mock_connect_db):
        # Setup mock
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = ('file.mp4',)
        mock_connect_db.return_value = (MagicMock(), mock_cursor)

        # Call the function
        result = check_file_exists('hash')

        # Assert the result
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
