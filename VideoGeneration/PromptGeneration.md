## Prompt Generation ##

You need to generate a prompt to instruct a video model to generate a subsequent video based on the last frame of a given natural video.  You need to ensure that the expanded video should differ significantly from the previous video to make a big difference between raw video and AI-extended part.The focus should be on quickly generating movements that differ from natural laws and common sense, ensuring that humans can react quickly without causing drastic changes in the visuals.

We will provide:

1. A description of the video:
2. Five keywords related to the video:

You need to accept these Requirements:

Requirement 1: The prompt should satisfy: Subject + Background + Movement. Subject**:** This refers to the main characters, animals, objects, etc., in the frame. Movement**:** This indicates the desired trajectory of the target subject. Background**:** This refers to the setting or environment depicted in the frame. For example, if you want to "have the Mona Lisa wear sunglasses," simply inputting "wear sunglasses" might make it difficult for the model to understand the instruction. As a result, it may generate a video based on its own interpretation. When the model identifies this as a painting, it is more likely to create a video featuring a moving exhibition of the artwork. This is also why still images often lead to the generation of static videos. Therefore, we need to describe "Subject + Movement" to help the model understand the instruction, such as "the Mona Lisa puts on sunglasses with her hand," or for multiple subjects, "the Mona Lisa puts on sunglasses with her hand, and a beam of light appears in the background." This way, the model will be more likely to respond accurately.

Requirement 2: Generate a description prompt only, no additional information needed. Within 120 characters, including spaces and punctuation. Please answer in English.

Requirement 3: You need to carefully read the "A description of the video" and the keywords. Your expansion should be based on them and try not to deviate too much.
