import os
import pickle

# 사용자정의 함수부
def input_scores():
    scores = []
    for i in range(3):
        score = int(input(f" {i+1}? "))
        if score == -1:
            break
        scores.append(score)
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def print_scores_and_average(scores, average):
    print("[점수 출력]")
    if scores:
        print("입력 점수:", " ".join(map(str, scores)))
        print(f"평균: {average:.1f}")
    else:
        print("입력된 점수가 없습니다.")

def save_scores(scores, filename):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return

# 프로그래밍 실행부
def main():
    filename = "score.bin"
    
    # 파일에서 점수 읽기
    loaded_scores = load_scores(filename)
    if loaded_scores is not None:
        print("[파일 읽기]")
        loaded_average = calculate_average(loaded_scores)
        print_scores_and_average(loaded_scores, loaded_average)
    else:
        print("[점수 입력]")
        scores = input_scores()
        average = calculate_average(scores)
        print_scores_and_average(scores, average)
        save_scores(scores, filename)

if __name__ == "__main__":
    main()
