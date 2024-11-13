x=
y=

model=sequential()
model.add(Dense(10,input_dim=10,activation='relu'))
model.add(Dense(5,activation='relu'))
model.add(Dense(1,activation='relu'))

model.compile(optimizer=Adam(learning_rate=0.001),loss=)

loss=model.fit(x,y,epochs=100)

predictions=model.
print(mean_squared_error(y,predicted))