from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext 
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class DatabaseConn:
    """A fake database to get customers' info"""
    @classmethod
    async def cust_name(cls, *, id: int) -> str | None:
        """Returns a mock name for a specific customer ID"""
        if id == 123:
            return 'John'
    
    @classmethod
    async def cust_bal(cls, *, id: int, include_pending: bool) -> float:
        """Returns a balance: either 123.45 (with pending transactions) or 100.00 (without)"""
        if id == 123:
            if include_pending:
                return 123.45
            else:
                return 100.00
        else:
            raise ValueError('Customer not found.')
            
@dataclass # Used to define simple data structures 
class SupportDependencies:
    """External dependencies required by agent: Customer ID and a database connection"""
    cust_id: int
    db: DatabaseConn
    
class SupportOutput(BaseModel):
    """Structured Output from the agent"""
    support_advice: str = Field(description='Advice returned to the customer.')
    block_card: bool = Field(description='Whether to block their card or not.')
    risk: int = Field(description='Risk level of query', ge=0, le=10)
    
# 
support_agent = Agent(
    model='openai:gpt-4o-mini',
    deps_type=SupportDependencies,
    output_type=SupportOutput,
    system_prompt="""
    You are a support agent in our bank. Give the customer support and 
    judge the risk level of their query. Reply using the customer's name.
    """
)

# System Prompt Modifier: Adds dynamic info to the prompt before the agent runs
@support_agent.system_prompt 
async def add_cust_name(ctx: RunContext[SupportDependencies]) -> str:
    """Returns the customer's name by pulling it from the database and adding it to the sys prompt"""
    cust_name = await ctx.deps.db.cust_name(id=ctx.deps.cust_id)
    return f"The customer's name is {cust_name!r}"
    
# Tool: Used by agent to check the balance of customer
@support_agent.tool
async def cust_bal(ctx: RunContext[SupportDependencies], include_pending: bool) -> str:
    """Returns the customer's current account balance."""
    balance = await ctx.deps.db.cust_bal(
        id = ctx.deps.cust_id,
        include_pending=include_pending
    )
    return f'${balance: .2f}'
    
if __name__=="__main__":
    
    # Dependencies that are passed to the agent
    deps = SupportDependencies(cust_id=123, db=DatabaseConn())
    
    # The agent receives the prompt, calls cust_bal() internally, and returns structured advice.
    result1 = support_agent.run_sync(
        'What is my balance?',
        deps=deps
    )
    print(result1.output)
    
    """support_advice='Your current account balance is $123.45.' block_card=False risk=1"""
    
    result2 = support_agent.run_sync(
        'I just lost my wallet, so my debit card.',
        deps=deps
    )
    print(result2.output)
    """support_advice="It's essential to block your card immediately to prevent unauthorized transactions. Please contact customer service or use the banking app to block your card." block_card=True risk=8"""