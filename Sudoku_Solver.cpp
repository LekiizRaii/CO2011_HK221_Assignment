#include<bits/stdc++.h>
using namespace std;
class Solve_Sudoku
{
    private:
        int** _board; //Contain result
        bool** _index_columns; //Check if a value exists in specified column
        bool** _index_rows; //Check if a value exists in specified row
        bool** _index_parts; //Check if a value exists in specified parted - square
        bool _no_solution = false; //Check if there is any solution
        bool _stop = false; //Whether a solution is found
        bool _have_fit = false; //Check if need-to-solve matrix has been fitted

        //Get the square which x, y belong to
        int _get_part(int x, int y)
        {
            return (((x - 1) / 3) * 3) + ((y - 1) / 3 + 1);
        }

        //Check whether the value is accecptable
        bool _check(int x, int y, int value)
        {
            if(_index_columns[value][y])
            {
                return false;
            }
            else
            {
                if(_index_rows[value][x])
                {
                    return false;
                }
                else
                {
                    if(_index_parts[value][_get_part(x, y)])
                    {
                        return false;
                    }
                    else return true;
                }
            }
        }

        //Get the specific position from a encoded id
        pair<int, int> _get_pos(int id)
        {
            return pair<int, int> ((id - 1) / 9 + 1, (id - 1) % 9 + 1);
        }

        //Insert a value into board
        void _insert(int x, int y, int value)
        {
            _board[x][y] = value;
            _index_columns[value][y] = 1;
            _index_rows[value][x] = 1;
            _index_parts[value][_get_part(x, y)] = 1;
        }

        //Erase a value from board
        void _erase(int x, int y, int value)
        {
            _board[x][y] = 0;
            _index_columns[value][y] = 0;
            _index_rows[value][x] = 0;
            _index_parts[value][_get_part(x, y)] = 0;
        }

        //Main algorithm
        void _back_tracking(int id)
        {
            pair<int, int> pos = _get_pos(id);
            if(_board[pos.first][pos.second] != 0)
            {
                if(id < 81) _back_tracking(id + 1);
                else
                {
                    _stop = true;
                    return ;
                }
            }
            else
            {
                for(int value = 1; value <= 9; value++)
                {
                    if(_check(pos.first, pos.second, value))
                    {
                        if(id < 81)
                        {
                            _insert(pos.first, pos.second, value);
                            _back_tracking(id + 1);
                            if(_stop) return ;
                            _erase(pos.first, pos.second, value);
                        }
                        else
                        {
                            _insert(pos.first, pos.second, value);
                            _stop = true;
                            return ;
                        }
                    }
                }
            }
        }

        
    public:

        //Create necessary matrixes
        Solve_Sudoku()
        {
            _board = new int*[10];
            _index_columns = new bool*[10];
            _index_rows = new bool*[10];
            _index_parts = new bool*[10];

            for(int i = 0; i <= 9; i++)
            {
                _board[i] = new int[10];
                _index_columns[i] = new bool[10];
                _index_rows[i] = new bool[10];
                _index_parts[i] = new bool[10];
            }
        }

        //Solve the problem from given values
        void _fit(int** values)
        {
            _have_fit = true;
            for(int i = 1; i <= 9; i++)
            {
                for(int j = 1; j <= 9; j++)
                {
                    _index_columns[i][j] = 0;
                    _index_rows[i][j] = 0;
                    _index_parts[i][j] = 0;
                }
            }
            for(int i = 1; i <= 9; i++)
            {
                for(int j = 1; j <= 9; j++)
                {
                    _board[i][j] = values[i][j];
                    if(values[i][j])
                    {
                        _index_columns[values[i][j]][j] = 1;
                        _index_rows[values[i][j]][i] = 1;
                        _index_parts[values[i][j]][_get_part(i, j)] = 1;
                    }
                }
            }
            _back_tracking(1);
        }

        //Display result
        void _result()
        {
            if(!_have_fit)
            {
                cout << "Haven't fitted yet";
                return ;
            }
            if(_no_solution) cout << "No Solution";
            else
            {
                cout << "My solution: " << endl;
                for(int i = 1; i <= 9; i++)
                {
                    if(i % 3 == 1)
                    {
                        for(int j = 1; j <= 25; j++) cout << "-";
                        cout << endl;
                    }
                    for(int j = 1; j <= 9; j++)
                    {
                        if(j % 3 == 1) cout << "| ";
                        cout << _board[i][j] << " ";
                    }
                    cout << "|" << endl;
                }
                for(int i = 1; i <= 25; i++) cout << "-";
            }
        }

        ~Solve_Sudoku()
        {
            for(int i = 0; i <= 9; i++)
            {
                delete[] _board[i];
                delete[] _index_columns[i];
                delete[] _index_rows[i];
                delete[] _index_parts[i];
            }
        }

};

int main()
{
    freopen("Sudoku_input.inp", "r", stdin);
    int** values;
    values = new int*[10];
    for(int i = 0; i <= 9; i++) values[i] = new int[10];
    for(int i = 1; i <= 9; i++)
    {
        for(int j = 1; j <= 9; j++)
        {
            cin >> values[i][j];
        }
    }

    Solve_Sudoku model;
    model._fit(values);
    model._result();
    return 0;
}