import requests

roomcode = input("Room Code: ")

room = requests.post('https://game.quizizz.com/play-api/v5/checkRoom', json={"roomCode": roomcode})
data = room.json().get('room')
roomhash = data.get('hash')

if 'error' in data:
	print("Invalid Quizizz Code!")
else:
	print("Powerup list: 2x, streak-saver, double-jeopardy, 50-50, eraser, immunity, time-freeze, power-play, glitch")
	username = input("Username: ")
	while True:
		powerup = input("Powerup name: ")
		add = requests.post('https://game.quizizz.com/play-api/awardPowerup', json={"roomHash": roomhash,"playerId": username,"powerup":{"name": powerup},"gameType": "live"})
		if add.status_code == 200:
			print("Success")
		else:
			print("Failure")
