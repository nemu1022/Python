def function_a():
    print('関数Aを実行')
    function_b()
    function_c()

def function_b():
    print('関数Bを実行')

def function_c():
    print('関数Cを実行')

function_a()