import aiohttp,asyncio
class AsyncTrendymanga():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://api.trendymanga.com"
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def login(self,email,password):
		data={"username":email,"password":password}
		async with self.session.post(f"{self.api}/auth/login",json=data,headers=self.headers) as req:
			data=await req.json()
			self.headers["Authorization"]=data["access_token"]
			return data
	async def register(self,email,password,username):
		data={"email":email,"password":password,"username":username}
		async with self.session.post(f"{self.api}/auth/register",json=data,headers=self.headers) as req:
			return await req.json()
	async def search(self,page:int=1,size:int=50,artist:str=None,name:str=None,author:str=None,tags:str=None,publishers:str=None):
		data={"page":page,"limit":size,"sortBy":"CREATED_AT","direction":"desc","author":"","artist":"","name":"","publishers":"","tags":""}
		if artist:data["artist"]=artist
		if name:data["name"]=name
		if author:data["author"]=author
		if tags:data["tags"]=[tags]
		if publishers:data["publishers"]=[publishers]
		async with self.session.post(f"{self.api}/titles/search",json=data,headers=self.headers) as req:
			return await req.json()
	async def comment(self,title_id,message):
		data={"titleId":title_id,"text":message}
		async with self.session.post(f"{self.api}/comments",json=data,headers=self.headers) as req:
			return await req.json()
	async def comment_list():
		async with self.session.get(f"{self.api}/comments/title/{title_id}",headers=self.headers) as req:
			return await req.json()
	async def reply_comment(self,comment_id,message):
		data={"titleId":title_id,"text":message}
		async with self.session.post(f"{self.api}/comments/{comment_id}/reply",json=data,headers=self.headers) as req:
			return await req.json()
	async def vote_comment(self,comment_id):
		async with self.session.post(f"{self.api}/comments/{comment_id}/upvote",headers=self.headers) as req:
			return req.json()
	async def unvote_comment(self,comment_id):
		async with self.session.post(f"{self.api}/comments/{comment_id}/downvote",headers=self.headers) as req:
			return req.json()
	async def chapters_like(self,chapters_id,title_id):
		async with self.session.post(f"{self.api}/titles/{title_id}/chapters/{chapters_id}/like",headers=self.headers) as req:
			return req.json()
	async def bookmark(self,type,title_id):
		data={"type":type}
		async with self.session.post(f"{self.api}/titles/{title_id}/bookmark",json=data,headers=self.headers) as req:
			return req.text()
	async def tags_list(self,size:int=10,start:int=0):
		async with self.session.get(f"{self.api}/tags?offset={start}&limit={size}",headers=self.headers) as req:
			return await req.json()
	async def genres_list(self,size:int=10,start:int=0):
		async with self.session.get(f"{self.api}/genres?offset={start}&limit={size}",headers=self.headers) as req:
			return await req.json()
	async def publishers(self,size:int=10,start:int=0):
		async with self.session.get(f"{self.api}/publishers?offset={start}&limit={size}",headers=self.headers) as req:
			return await req.json()
	async def top_titles(self,size:int=10):
		async with self.session.get(f"{self.api}/titles/top?period=all-time&limit={size}",headers=self.headers) as req:
			return await req.json()
	async def last_updates(self,size:int=10,start:int=0):
		async with self.session.get(f"{self.api}/titles/lastUpdates?limit={size}&offset={start}",headers=self.headers) as req:
			return await req.json()