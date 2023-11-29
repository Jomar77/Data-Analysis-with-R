from elevenlabs import save, generate, play, set_api_key, clone

set_api_key("78aa8e037c1ba1f942892b76c658d233")


voice = clone(
    name="Alex",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
    files=[ "music/sample (2).wav", "music/sample (3).wav", "music/sample (1).m4a", "music/sample (4).m4a" ]
    
)



audio = generate(text="I'm not a doctor, but the symptoms you described, such as intermittent tingling in the left side of the back, intermittent shortness of breath, and intermittent sharp pains in the heart region, could potentially be associated with various conditions. These might include issues with the spine, respiratory system, or cardiovascular system. However, a precise diagnosis would require a thorough examination, medical history review, and possibly diagnostic tests. It's important to consult with a healthcare professional for an accurate assessment and appropriate guidance.", voice=voice)


save(audio, "demo.wav")

audio = generate(text="제가 의사는 아니지만, 여러 증상을 설명한 것은 왼쪽 등의 간헐적인 쏠림, 간헐적인 호흡 곤란, 그리고 가슴 부위에서의 간헐적인 날카로운 통증과 관련이 있을 수 있습니다. 이는 척추, 호흡 기계, 또는 심혈관 시스템과 관련된 문제일 수 있습니다. 그러나 정확한 진단을 위해서는 철저한 검사, 병력 확인, 그리고 필요한 경우 진단 테스트가 필요합니다. 정확한 평가와 적절한 안내를 위해 의료 전문가와 상담하는 것이 중요합니다.", voice=voice, model="eleven_multilingual_v2")
save(audio, "demo_kor.wav")

play(audio)



# voices = voices()
# audio = generate(text="Hello there!", voice=voices[0])
# print(voices)

