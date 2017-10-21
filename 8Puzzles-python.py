# Nguyen Duy Khuong
# mang chua gia tri ban dau
_init_state = [[7,2,4],
               [5,0,6],
               [8,3,1]]
_stt = [[0,0,0],
        [0,0,0],
        [0,0,0]]
# Dinh nghia lop chua trang thai cua game
class EightPuzzle:
    _state = [] # mang chua gia tri
    _hang = 0 # luu vi tri hang hien tai cua o trong
    _cot = 0 # luu vi tri cot hien tai cua o trong
    # ham khoi tao
    def __init__(self,_hang,_cot,_state):
        self._hang = _hang
        self._cot = _cot
        self._state = []
        # gan gia tri mau vao mang
        for i in range(3):
            self._state.append(_state[i][:])
    # ham them gia tri _value vao mang _state tai [_hang][_cot]        
    def set_value(self,_hang,_cot,_value):
        self._state[_hang][_cot] = _value
        
    def show(self):
        for i in range(3):
            print(self._state[i][:])
        print('\n')
            

def move_left(puz_a,puz_b): # puz_a trang thai ban dau
    if puz_a._cot == 0:# neu o trong dang tai cot dau tien => tra ve -1 va ngung xu ly
        return -1
    # gan gia tri tu puz_a vao puz_b
    for row in range(3):
            for col in range(3):
                puz_b._state[row][col] = puz_a._state[row][col]
                
    i = puz_a._hang
    j = puz_a._cot
    
    # Khi di chuyen o trong qua trai, gia tri cot hien tai giam 1 j=j-1
    
    # luu gia tri tai o trong trong puz_b vao bien tam temp
    temp = puz_b._state[i][j]
    # gan gia tri cua puz_b tai vi tri hang i cot j bang gia tri cua puz_a tai vi tri [i][j-1]
    puz_b.set_value(i,j,puz_a._state[i][j-1])
    # gan gia tri cua puz_b tai vi tri hang i cot j-1 bang gia tri cua bien tam temp
    puz_b.set_value(i,j-1,temp)
    # Cap nhat lai vi tri hang va cot cho puz_b
    puz_b._hang = i
    puz_b._cot = j-1
    puz_b.show()

def move_right(puz_a,puz_b): # puz_a trang thai ban dau
    if puz_a._cot == 2:# neu o trong dang tai cot cuoi => tra ve -1 va ngung xu ly
        return -1
    # gan gia tri tu puz_a vao puz_b
    for row in range(3):
            for col in range(3):
                puz_b._state[row][col] = puz_a._state[row][col]
    i = puz_a._hang
    j = puz_a._cot

    # Khi di chuyen o trong qua trai, gia tri cot hien tai tang 1 j=j+1
    
    # luu gia tri tai o trong trong puz_b vao bien tam temp
    temp = puz_b._state[i][j]
    # gan gia tri cua puz_b tai vi tri hang i cot j bang gia tri cua puz_a tai vi tri [i][j+1]
    puz_b.set_value(i,j,puz_a._state[i][j+1])
    # gan gia tri cua puz_b tai vi tri hang i cot j+1 bang gia tri cua bien tam temp
    puz_b.set_value(i,j+1,temp)
    # Cap nhat lai vi tri hang va cot cho puz_b
    puz_b._hang = i
    puz_b._cot = j+1
    puz_b.show()

def move_up(puz_a,puz_b): # puz_a trang thai ban dau
    if puz_a._hang == 0:
        return -1
    for row in range(3):
            for col in range(3):
                puz_b._state[row][col] = puz_a._state[row][col]
    i = puz_a._hang
    j = puz_a._cot

    # Khi di chuyen o trong len tren, gia tri hang hien tai giam 1 i=i-1
    
    temp = puz_b._state[i][j] # luu gia tri tai o trong vao bien tam
    puz_b.set_value(i,j,puz_a._state[i-1][j])
    puz_b.set_value(i-1,j,temp)
    puz_b._hang = i-1
    puz_b._cot = j
    puz_b.show()

def move_down(puz_a,puz_b): # puz_a trang thai ban dau
    if puz_a._hang == 2:
        return -1
    for row in range(3):
            for col in range(3):
                puz_b._state[row][col] = puz_a._state[row][col]
    i = puz_a._hang
    j = puz_a._cot

    # Khi di chuyen o trong xuong duoi, gia tri hang hien tai tang 1 i=i+1
    
    temp = puz_b._state[i][j] # luu gia tri tai o trong vao bien tam
    puz_b.set_value(i,j,puz_a._state[i+1][j])
    puz_b.set_value(i+1,j,temp)
    puz_b._hang = i+1
    puz_b._cot = j
    puz_b.show()
    
puzzel = EightPuzzle(1,1,_init_state)
puzzel1  = EightPuzzle(0,0,_stt)
print("Trang thai ban dau:")
puzzel.show()
print("Di chuyen o trong qua trai:")
move_left(puzzel,puzzel1)
print("Di chuyen o trong qua phai:")
move_right(puzzel,puzzel1)
print("Di chuyen o trong len tren:")
move_up(puzzel,puzzel1)
print("Di chuyen o trong xuong duoi:")
move_down(puzzel,puzzel1)

