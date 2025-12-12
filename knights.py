import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import time

class KnightsTour:
    def __init__(self, board_size=8, closed_tour=False):
        """
        Initialize Knight's Tour solver
        
        Parameters:
        - board_size: ukuran papan (default 8x8)
        - closed_tour: True untuk closed tour, False untuk open tour
        """
        self.size = board_size
        self.closed_tour = closed_tour
        self.board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
        
        # Knight's possible moves (L-shaped: 2 squares in one direction, 1 in perpendicular)
        self.moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
        
        self.solution_time = 0
        
    def is_safe(self, x, y):
        """Check if position is valid and unvisited"""
        return (0 <= x < self.size and 
                0 <= y < self.size and 
                self.board[x][y] == -1)
    
    def count_unvisited_neighbors(self, x, y):
        """Count unvisited neighbors (Warnsdorff's heuristic)"""
        count = 0
        for i in range(8):
            next_x = x + self.moves_x[i]
            next_y = y + self.moves_y[i]
            if self.is_safe(next_x, next_y):
                count += 1
        return count
    
    def solve_tour(self, start_x=0, start_y=0):
        """
        Solve Knight's Tour using backtracking with Warnsdorff's heuristic
        
        Parameters:
        - start_x: posisi x awal (baris)
        - start_y: posisi y awal (kolom)
        
        Returns:
        - True jika solusi ditemukan, False jika tidak
        """
        start_time = time.time()
        
        # Initialize
        self.board = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        self.board[start_x][start_y] = 0
        
        result = self._solve_util(start_x, start_y, 1, start_x, start_y)
        
        self.solution_time = time.time() - start_time
        return result
    
    def _solve_util(self, x, y, move_count, start_x, start_y):
        """Recursive backtracking with Warnsdorff's heuristic"""
        # If all squares visited
        if move_count == self.size * self.size:
            # For closed tour, check if knight can return to start
            if self.closed_tour:
                for i in range(8):
                    if (x + self.moves_x[i] == start_x and 
                        y + self.moves_y[i] == start_y):
                        return True
                return False
            return True
        
        # Get all possible moves and sort by Warnsdorff's heuristic
        moves = []
        for i in range(8):
            next_x = x + self.moves_x[i]
            next_y = y + self.moves_y[i]
            if self.is_safe(next_x, next_y):
                priority = self.count_unvisited_neighbors(next_x, next_y)
                moves.append((priority, next_x, next_y))
        
        # Sort by priority (fewer unvisited neighbors first)
        moves.sort()
        
        # Try each move
        for _, next_x, next_y in moves:
            self.board[next_x][next_y] = move_count
            
            if self._solve_util(next_x, next_y, move_count + 1, start_x, start_y):
                return True
            
            # Backtrack
            self.board[next_x][next_y] = -1
        
        return False
    
    def visualize(self, save_fig=False, filename='knights_tour.png'):
        """
        Visualize the knight's tour
        
        Parameters:
        - save_fig: jika True, simpan gambar
        - filename: nama file untuk menyimpan gambar
        """
        if self.board[0][0] == -1:
            print("No solution found!")
            return
        
        fig, ax = plt.subplots(figsize=(12, 12))
        
        # Create chessboard pattern
        for i in range(self.size):
            for j in range(self.size):
                color = '#F0D9B5' if (i + j) % 2 == 0 else '#B58863'
                ax.add_patch(Rectangle((j, self.size-1-i), 1, 1, 
                                      facecolor=color, edgecolor='black', linewidth=1))
                
                # Add move numbers
                if self.board[i][j] != -1:
                    ax.text(j + 0.5, self.size - 1 - i + 0.5, 
                           str(self.board[i][j]),
                           ha='center', va='center', 
                           fontsize=10, fontweight='bold',
                           color='black', bbox=dict(boxstyle='round,pad=0.3', 
                                                   facecolor='white', alpha=0.7))
        
        # Draw the path
        path = []
        for move in range(self.size * self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == move:
                        path.append((j + 0.5, self.size - 1 - i + 0.5))
        
        if path:
            path_x, path_y = zip(*path)
            ax.plot(path_x, path_y, 'r-', linewidth=2.5, alpha=0.5, label='Path')
            
            # Mark start position
            ax.plot(path_x[0], path_y[0], 'go', markersize=15, label='Start', zorder=5)
            
            # Mark end position
            ax.plot(path_x[-1], path_y[-1], 'bs', markersize=15, label='End', zorder=5)
            
            # For closed tour, connect end to start
            if self.closed_tour:
                ax.plot([path_x[-1], path_x[0]], [path_y[-1], path_y[0]], 
                       'r--', linewidth=2.5, alpha=0.5, label='Return to Start')
        
        ax.set_xlim(0, self.size)
        ax.set_ylim(0, self.size)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        
        tour_type = "Closed Tour" if self.closed_tour else "Open Tour"
        plt.title(f"Knight's Tour ({tour_type}) - {self.size}x{self.size} Board\nSolution Time: {self.solution_time:.4f}s", 
                 fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        
        if save_fig:
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"Gambar disimpan sebagai {filename}")
        
        plt.show()
    
    def print_board(self):
        """Print the board in console"""
        if self.board[0][0] == -1:
            print("No solution found!")
            return
        
        tour_type = "CLOSED TOUR" if self.closed_tour else "OPEN TOUR"
        print(f"\n{tour_type} - Knight's Tour Solution:")
        print("=" * (self.size * 4 + 1))
        
        for i in range(self.size):
            for j in range(self.size):
                print(f"{self.board[i][j]:3d}", end=" ")
            print()
        print("=" * (self.size * 4 + 1))
        print(f"Solution time: {self.solution_time:.4f} seconds")
    
    def get_path_coordinates(self):
        """
        Get path coordinates in move order
        
        Returns:
        - List of tuples (x, y) representing the path
        """
        path = []
        for move in range(self.size * self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == move:
                        path.append((i, j))
        return path


# Example usage
if __name__ == "__main__":
    print("TUGAS PRAKTIKUM - THE KNIGHT'S TOUR")
    print("=" * 50)
    
    # Situation a: Open Tour
    print("\nSituation A: Open Tour (ending at any square)")
    print("-" * 50)
    knight_open = KnightsTour(board_size=8, closed_tour=False)
    
    if knight_open.solve_tour(start_x=0, start_y=0):
        print("✓ Solution found for Open Tour!")
        knight_open.print_board()
        knight_open.visualize()
    else:
        print("✗ No solution found for Open Tour")
    
    # Situation b: Closed Tour
    print("\nSituation B: Closed Tour (returning to starting square)")
    print("-" * 50)
    knight_closed = KnightsTour(board_size=8, closed_tour=True)
    
    if knight_closed.solve_tour(start_x=0, start_y=0):
        print("✓ Solution found for Closed Tour!")
        knight_closed.print_board()
        knight_closed.visualize()
    else:
        print("✗ No solution found for Closed Tour")
    
    print("\nNote: You can change the starting position by modifying")
    print("the start_x and start_y parameters in solve_tour()")