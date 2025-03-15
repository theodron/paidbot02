from bot import Bot

Bot().run()
invite_link = bot.exportChatInviteLink(chat_id="-100252317432")
print(invite_link)
print(f"Force Sub Channel: {FORCE_SUB_CHANNEL_2}")
print(f"Bot permissions: {bot.getChat(FORCE_SUB_CHANNEL_2)}")
