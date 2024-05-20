import aiopg
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
class Database:
    def __init__(self, dsn):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        print('Conectando ao banco de dados...')
        self.pool = await aiopg.create_pool(self.dsn)

    async def disconnect(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    async def execute(self, query, *args):
        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(query, *args)
                await connection.commit()

    async def fetch(self, query, *args):
        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(query, *args)
                return await cursor.fetchall()

db = Database(os.getenv('DATABASE_URL'))


async def init_db():
    print('Banco de dados conectado!')
    await db.connect()
    

async def close_db():
    await db.disconnect()

# Exemplo de uso
async def main():
    await init_db()
    # Execute suas consultas ou operações com o banco de dados aqui
    await close_db()

# Execute o loop de evento do asyncio para executar o programa
if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
