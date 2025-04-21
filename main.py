class Matrix:
    def __init__(self, rows, cols, data=None):
        """
        Инициализация матрицы.
        :param rows: количество строк
        :param cols: количество столбцов
        :param data: данные матрицы (двумерный список, необязательный)
        """
        self.rows = rows
        self.cols = cols
        
        if data is not None:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError("Несоответствие размеров данных и матрицы")
            self.data = data
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def __str__(self):
        """Строковое представление матрицы."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def __add__(self, other):
        """Сложение матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для сложения")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    
    def __sub__(self, other):
        """Вычитание матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для вычитания")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        """Умножение матриц или умножение матрицы на скаляр."""
        if isinstance(other, (int, float)):
            # Умножение на скаляр
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        elif isinstance(other, Matrix):
            # Умножение матриц
            if self.cols != other.rows:
                raise ValueError(
                    "Количество столбцов первой матрицы должно быть равно количеству строк второй"
                )
            
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise TypeError("Неподдерживаемый тип для умножения")
