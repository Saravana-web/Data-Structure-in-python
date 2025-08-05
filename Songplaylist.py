class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.current=None

    def get_length(self):
        temp, count = self.head, 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def create_playlist(self, song_list):
        for title in song_list:
            self.insert_song(title)

    def insert_song(self, title):
        new_node = SongNode(title)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Song '{title}' added to the playlist.")

    def delete_song(self, title):
        temp = self.head
        prev = None

        while temp:
            if temp.title == title:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Song '{title}' deleted from the playlist.")
                return
            prev = temp
            temp = temp.next
        print(f"Song '{title}' not found in the playlist.")

    def insert_beginning(self, title):
        node = SongNode(title)
        node.next = self.head
        self.head = node
        if not self.current:
            self.current = node
        print(f"'{title}' added at the beginning.")

    def insert_end(self, title):
        node = SongNode(title)
        if not self.head:
            self.head = self.current = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        print(f"'{title}' added at the end.")

    def insert_pos(self, title, pos):
        if pos < 1:
            print("Invalid position! Must be 1 or more.")
            return
        length = self.get_length()
        if pos > length + 1:
            print(f"Invalid position! Playlist has {length} song(s). Insert at 1 to {length + 1}.")
            return
        if pos == 1:
            self.insert_beginning(title)
            return
        node = SongNode(title)
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
        node.next = temp.next
        temp.next = node
        print(f"'{title}' inserted at position {pos}.")

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        print("Music Playlist:")
        temp = self.head
        while temp:
            print(f"{temp.title}")
            temp = temp.next

    def search_song(self, title):
        temp = self.head
        prev = None

        while temp:
            if temp.title == title:
                print(f"Song '{title}' found in the playlist.")
                return
            prev = temp
            temp = temp.next
        print(f"Song '{title}' not found in the playlist.")


def main():
    playlist = MusicPlaylist()

    while True:
        print("\n--- Music Playlist Menu ---")
        print("1. Create Playlist")
        print("2. Insert Song at a position")
        print("3. Delete Song")
        print("4. Display Playlist")
        print("5. search Playlist")
        print("6. Exit")
        

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            songs = input("Enter song titles separated by commas: ").split(",")
            songs = [song.strip() for song in songs]
            playlist.create_playlist(songs)
        elif choice == "2":
            title = input("Enter song title: ")
            print("Where to insert?\n1. Beginning\n2. End\n3. Specific Position")
            loc = input("Enter choice: ")
            if loc == "1":
                playlist.insert_beginning(title)
            elif loc == "2":
                playlist.insert_end(title)
            elif loc == "3":
                try:
                    pos = int(input("Enter position: "))
                    playlist.insert_pos(title, pos)
                except:
                    print("Enter a valid number.")
        elif choice == '3':
            title = input("Enter song title to delete: ").strip()
            playlist.delete_song(title)
        elif choice == '4':
            playlist.display_playlist()
        elif choice == '5':
            title = input("Enter song title to search: ").strip()
            playlist.search_song(title)
            break
        elif choice == '6':
            print("Exiting Music Playlist. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
