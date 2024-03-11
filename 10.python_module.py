print('>>>> Example - 1 >>>>')
# Load module example.
import module_example as ex

print('Module (', ex.__name__, ') successfully loaded.')
print('Module directory : ', dir(ex))

print('Addition :', ex.add(4, 5))
print('Subtraction :', ex.sub(4, 5))
print('Division :', ex.div(4, 5))
print('Multiply :', ex.mul(4, 5))

print('\n')
print('>>>> Example - 2 >>>>')
# Load module (information) from package (store).
from store import information as info

print('Package (', info.__package__, ') successfully loaded.')
print('Module (', info.__name__, ') successfully loaded.')
print('Module directory : ', dir(info))
print('Store Message :', info.msg())
