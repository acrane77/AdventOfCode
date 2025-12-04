#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int part1(const std::vector<std::vector<char>>& grid) {
    int total = 0;
    int dirx[8] = { 0, 1, 1, 1, 0, -1, -1, -1 }; // Direction matrices for checking 3x3 grid
    int diry[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };

    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] == '@') {
                int count = 0;
                int running_total = 5; // for edge-checking; problem states "fewer than 4 '@' neighbors" meaning atleast 5 '.' neighbors

                for (int k = 0; k < 8; k++) { // k must select which position of calculation array we will use
                    int pos1 = dirx[k];
                    int pos2 = diry[k];
                    
                    int r = pos1 + i;
                    int c = pos2 + j;

                    if (r >= 0 && r < grid.size() && c >= 0 && c < grid[r].size() && grid[r][c] == '.') count++; // Increment count when in the middle and a . is in 3x3 grid.
                    else if (r < 0 || r >= grid.size() || c < 0 || c >= grid[r].size()) running_total--; // Decrement running total when on the edge of the grid
                    
                    if (count >= running_total) {
                        total++;
                        break;
                    }
                }
            }
        }
    }
    return total;
}

int part2(std::vector<std::vector<char>>& grid) { 
    int total = 0;
    
    int dirx[8] = { 0, 1, 1, 1, 0, -1, -1, -1 }; 
    int diry[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };
    int mutations = 1;

    while (mutations > 0) { // Recurse until we don't change the grid
        mutations = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == '@') {
                    int count = 0;
                    int running_total = 5; // Same neighbour count

                    for (int k = 0; k < 8; k++) {
                        int pos1 = dirx[k];
                        int pos2 = diry[k];

                        int r = pos1 + i;
                        int c = pos2 + j;

                        if (r >= 0 && r < grid.size() && c >= 0 && c < grid[r].size() && grid[r][c] == '.') count++; // Same conditions
                        else if (r < 0 || r >= grid.size() || c < 0 || c >= grid[r].size()) running_total--;         
                        
                        if (count >= running_total) { // If we find a valid removable object, remove it and repeat.
                            total++;
                            mutations++;
                            grid[i][j] = '.';
                            break;
                        }
                    }
                }
            }
        }
    }
    return total;
}


int main() {

    // Read file
    std::ifstream file;
    std::vector<std::vector<char>> grid;

    file.open("input4.txt");
    if (file.is_open()) {
        
        std::string line;
        while (std::getline(file, line)) {
            std::vector<char> row(line.begin(), line.end());
            grid.push_back(row);
        }

        file.close();
    }
    else {
        std::cout << "Error opening file. " << std::endl;
        return -1;
    }

    // Question calls
    int answer1 = part1(grid);
    int answer2 = part2(grid);

    std::cout << answer1 << std::endl;
    std::cout << answer2 << std::endl;
    return 1;
}