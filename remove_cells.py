from nbconvert.preprocessors import Preprocessor

class RemoveCellPreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, cell_index):
        # Check for the 'remove-cell' or 'remove-cell-output' tag
        if 'remove-cell' in cell.metadata.get('tags', []):
            return None, resources
        if 'remove-cell-output' in cell.metadata.get('tags', []):
            cell.outputs = []  # Remove outputs but keep the cell
        return cell, resources
