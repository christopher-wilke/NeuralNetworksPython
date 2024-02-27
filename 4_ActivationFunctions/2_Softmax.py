# Values from the previous output when we described what a neural network is
layer_outputs = [4.8, 1.21, -0.185]
E = 2.71828182486

exp_values = []
for output in layer_outputs:
    exp_values.append(E**output)

# Now normalize the values
norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)
print(f'Normalized values: {norm_values}')
