def use_db(func):
	def inner():
		print("Use Real DB")
		# ここに本番用DBの接続コードなどがある
		return func()
	return inner