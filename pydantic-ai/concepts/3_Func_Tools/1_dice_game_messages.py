from dice_game import dice_result

print(dice_result.all_messages())

"""
[
  ModelRequest(
    parts=
      [
        SystemPromptPart(
          content="You're a dice game, you should roll the die and see if the number you get matches the user's guess. If so, tell them they won. Use the player's name in the response.", 
          timestamp=datetime.datetime(2025, 7, 15, 17, 48, 47, 709344, tzinfo=datetime.timezone.utc)
        ), 
        UserPromptPart(
          content='My guess is 5', 
          timestamp=datetime.datetime(2025, 7, 15, 17, 48, 47, 709350, tzinfo=datetime.timezone.utc)
        )
      ]
    ), 
  ModelResponse(
    parts=
      [
        ToolCallPart(
          tool_name='roll_dice', 
          args={}, 
          tool_call_id='pyd_ai_dd375c2d6f9640ffa95d571900755cd3'
        ), 
        ToolCallPart(
          tool_name='get_player_name', 
          args={}, 
          tool_call_id='pyd_ai_c7b1eda58caa4164b225748e618f84ad'
        )
      ], 
    usage=Usage(requests=1, request_tokens=76, response_tokens=8, total_tokens=84, details={'text_candidates_tokens': 8, 'text_prompt_tokens': 76}), 
    model_name='gemini-2.0-flash', 
    timestamp=datetime.datetime(2025, 7, 15, 17, 48, 49, 913664, tzinfo=datetime.timezone.utc), 
    vendor_details={'finish_reason': 'STOP'}
  ), 
  ModelRequest(
    parts=
      [
        ToolReturnPart(
          tool_name='roll_dice', 
          content='6', 
          tool_call_id='pyd_ai_dd375c2d6f9640ffa95d571900755cd3', 
          timestamp=datetime.datetime(2025, 7, 15, 17, 48, 49, 916048, tzinfo=datetime.timezone.utc)
        ), 
        ToolReturnPart(
          tool_name='get_player_name', 
          content='8', 
          tool_call_id='pyd_ai_c7b1eda58caa4164b225748e618f84ad', 
          timestamp=datetime.datetime(2025, 7, 15, 17, 48, 49, 916650, tzinfo=datetime.timezone.utc)
        )
      ]
  ), 
  ModelResponse(
    parts=
      [
        TextPart(content='Tough luck, 8, you rolled a 6, and needed a 5. Better luck next time!\n')
      ], 
      usage=Usage(
        requests=1, 
        request_tokens=100, 
        response_tokens=24, 
        total_tokens=124, 
        details={
          'text_candidates_tokens': 24, 
          'text_prompt_tokens': 100
        }
      ), 
      model_name='gemini-2.0-flash', 
      timestamp=datetime.datetime(2025, 7, 15, 17, 48, 50, 892988, tzinfo=datetime.timezone.utc), 
      vendor_details={'finish_reason': 'STOP'}
  )
]
"""