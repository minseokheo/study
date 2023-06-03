import gym
import matplotlib.pyplot as plt

# 환경 불러오기
env=gym.make("FrozenLake-v1",is_slippery=False,render_mode='rgb_array')
print(env.observation_space)
print(env.action_space)

n_trial=20

# 에피소드 수집
env.reset()
episode=[]
output_image=[]
for i in range(n_trial):
    action=env.action_space.sample() # 행동을 취함(랜덤 선택)
    obs,reward,done,truncated,info=env.step(action) # 보상을 받고 상태가 바뀜
    episode.append([action,reward,obs])
    output_image.append(env.render())
    if done or truncated:
        break

print(episode)
env.close()

# 100개의 에피소드에서 목적지에 도착하는 경우 중단
for episode in range(100):
    env.reset()
    episode=[]
    output_image=[]
    for i in range(n_trial):
        action=env.action_space.sample() # 행동을 취함(랜덤 선택)
        obs,reward,done,truncated,info=env.step(action) # 보상을 받고 상태가 바뀜
        episode.append([action,reward,obs])
        output_image.append(env.render())
        if done or truncated:
            break
    if reward:
        break

print(episode)
env.close()

# Create a new figure
plt.figure(figsize=(15, 5))

# Display each image in a row
for i, img in enumerate(output_image):
    plt.subplot(2, (len(output_image)+1)//2, i+1)
    plt.imshow(img)
    plt.axis('off')