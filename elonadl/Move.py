import os
import shutil


class Move:
    def __init__(self, source_path, destination):
        self.source_path = source_path
        self.destination = destination
        
    def find_elona_directory(self) -> list:
        # Get all directories in the source path
        elona_dirs = []
        for item in os.listdir(self.source_path):
            item_path = os.path.join(self.source_path, item)

            if os.path.isdir(item_path) and item.startswith('Elona+'):
                elona_dirs.append(item_path)
                
        return elona_dirs
    
    def create_destination_directory(self):
        dest_path = os.path.join(self.source_path, self.destination)
        
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            print(f"Created destination directory: {dest_path}")
        
        return dest_path
    
    def move_files(self, elona_dir, dest_path) -> int:
        count = 0
        
        for item in os.listdir(elona_dir):
            source_item = os.path.join(elona_dir, item)
            dest_item = os.path.join(dest_path, item)
            
            # Handle file or directory
            try:
                if os.path.isfile(source_item):
                    shutil.copy2(source_item, dest_item)
                    count += 1
                elif os.path.isdir(source_item):
                    shutil.copytree(source_item, dest_item)
                    count += 1  # Count directory as one item
            except (shutil.Error, OSError) as e:
                print(f"Error moving {source_item}: {e}")
                
        return count
    
    def execute(self) -> dict:
        results = {
            "elona_dirs_found": [],
            "files_moved": 0,
            "success": False
        }
        
        # Find Elona+ directories
        elona_dirs = self.find_elona_directory()
        
        if not elona_dirs:
            print("No directories starting with 'Elona+' found.")
            return results
        
        results["elona_dirs_found"] = elona_dirs
        
        # Create destination directory
        dest_path = self.create_destination_directory()
        
        # Move files from each Elona+ directory
        total_moved = 0
        for elona_dir in elona_dirs:
            print(f"Moving files from {elona_dir} to {dest_path}")
            moved = self.move_files(elona_dir, dest_path)
            total_moved += moved
            print(f"Moved {moved} items from {os.path.basename(elona_dir)}")
        
        results["files_moved"] = total_moved
        results["success"] = total_moved > 0
        
        print(f"Operation complete. Moved {total_moved} items in total.")
        return results
