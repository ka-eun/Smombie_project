# Smombie_project

- 프로젝트 개요
> 스마트폰을 사용하는 보행자를 인식하여 알림 또는 주의를 주는 시스템   
> 자세인식 알고리즘을 통해 해당 자세를 하고 있는 사람을 인식하는 서비스 구축   
   
- 개발 목표   
> smombie를 자동으로 detect하는 소프트웨어 알고리즘 개발   
> smombie detection의 정확도 80%이상 달성하기   
   
- 개발 방법   
> 스마트폰 사용자의 사진, 동영상을 빅데이터화여 학습시키기   
> 스마트폰 사용자의 자세 분석을 통해 특징 찾기   
> openCV, xml, tensorflow 사용 예정   
 
 ------
 
# 20180716 : 동작 인식 개발 tool   
- Tensorflow      
> 데이터 흐름 프로그래밍(ex. neural network)을 위한 오픈소스 소프트웨어       

- CNN model
> Fully convolutional neural network   
> 화면을 여러 개의 영역으로 쪼개 특징을 분석한 후 원하는 특징과 매칭되면 맞다고 인식한다. 본래 인식을 할 때 shift가 일어나면 (대상의 위치가 상하좌우로 변하면) 영역이 달라져 인식이 어려워지는데, shift가 발생해도 인식할 수 있게 하는 것이 convolutional이다.    

- pedestrian detection
> 보행자 인식. 보행자의 포즈까지는 인식하지 않음   

# 20180717 : Neural network with Python   
- machine learning   
> 반복을 통해 원하는 output이 나오도록 training   
   
- sigmoid method   
> input값에 따라 0과 1사이의 output값을 출력함   
> 수치데이터를 output으로 가지기 위한 neural network의 최종 layer에서 activation method로 사용   

# 20180718 : Neural network with Python, openCV   
- classified output을 가지는 neural network   
   
- 패턴 학습 (패턴 인식)    
> input의 영역을 1차원 리스트로 입력, 각 패턴에 대하여 클래스 숫자를 할당   
   
- openCV   
> computer vision을 위한 라이브러리    
> openCV를 이용하여 영상처리를 거친 값을 training input으로 사용    
   
# 20180720 : 사진/동영상 배경 제거   
- moving object(보행자)를 input값으로 사용하기 위한 배경 제거 코드 작성   
> 배경만 찍은 사진과 사람이 같이 찍힌 사진 두 장의 픽셀을 비교하여 달라진 부분이 존재하면 그 부분의 픽셀만 출력   
   
# 20180723 : openPose 설치   
- openPose   
> library for real-time multi-person keypoint detection on openCV   
> 실시간으로 입력받은 동영상에서 보행자 포즈를 수치화한 값을 받아올 수 있음   
   
- openPose 설치   
> 사양에 맞는 그래픽카드(gpu)가 없어 실패   
   
 # 20180726 - 20180806 : Smombie 데이터 수집   
- 사진 데이터 수집   
> 신호등, 길거리 등에서 스마트폰을 이용하는 사람들의 사진 데이터 수집 (약 2000장)        
       
 # 20180807 : Smombie 데이터 수집 및 분류  
- 사진 데이터 수집   
> 신호등, 길거리 등에서 스마트폰을 이용하는 사람들의 동영상 데이터 수집 
    
- 데이터 분석 및 분류   
> 효과적인 데이터 학습을 위해 앞모습, 뒷모습 분류       
 # 20180808 - 20180809 : Smombie 데이터 편집   
- 데이터 편집   
> 스마트폰 사용자의 자세 사진을 사용하기 위해 사진 편집 (약 3000장)   
    
 # 20180813 : Smombie 데이터 분류   
- 데이터 분류 : 스마트폰을 사용하는 팔(왼쪽/오른쪽), 각도(정면/45도/90도)에 따라 분류   
> 1_0(왼팔 정면) : 130장   
> 1_45(왼팔 45도) : 586장   
> 1_90(왼팔 90도) : 198장   
> 2_0(양팔 정면) : 457장   
> 3_0(오른팔 정면) : 225장   
> 3_45(오른팔 45도) : 401장   
> 3_90(오른팔 90도) : 305장       
> 애매(분류 불가) : 88장   
> 뒷모습 : 219장      
    
# 20180814 : Smombie detector XML    
- smombie detector XML 만들기   
> Haar Cascade를 이용한 Object dection xml 사용   
> 분류된 데이터에 따라 총 7개의 smombie detector xml 제작   
    
- XML 파일 적용하기   
> + 검출된 영역에서 피부색의 범위가 아닌 부분 제거   
>> hsv를 이용하여 피부색 영역 추출하기 어려움   
    
> + haar fullbody detector xml를 적용한 범위 안에서 smombie detecor 적용   
>> 정확도 약 0에 수렴   
>> 가방, 다리 등 두개의 수직선이 있는 영역 모두 인식   
>> 기존의 haar fullbody xml의 정확도가 낮아 인식이 어렵다   
    
 # 20180816 : Image classification using tensorflow   
- Dog-Cat classification   
 > tensorflow를 이용한 training을 거쳐 최종적으로 dog/cat 두 class로 분류시키는 모델 실습   
     
 # 20180817 - 20180824 : Smombie classifier model   
- model 분석
     
> + atcivation method에 따라   
>> 마지막 layer를 제외한 layer : relu, leaky relu, elu   
>> 마지막 lyaer : binary_crossentropy (classify를 위해 사용하는 함수)   
     
> + dense에 따라   
>> 500   
>> 1500   
>> 2000   
     
> + epoch에 따라   
>> 100      
>> 200   

> + 2층의 layer를 추가한 후 early stopping callback 기능을 이용하였다    
>> val_acc에 early stopping을 적용하여 일정 횟수이상 증가하지 않으면 학습을 중단하도록 하였다     
>> early stopping with patience=5, dense 4200    
>> early stopping with patience=5, dense 1500      
>> early stopping with patience=5, dense 500      
>> early stopping with patience=10, dense 4000      
>> early stopping with patience=10, dense 4900        

> + 기존의 LeNet을 변경한 새로운 CNN을 이용하여 학습      
>> dense=4800, early stopping(patience=10) 고정     
>> 1. (conv conv pool) * 2 (conv pool) * 2 (dense) * 2      
>> 2. (conv pool) * 2 (conv conv pool) * 2 (dense) * 2      
>> 3. (conv conv pool) * 3 (dense) * 2      
>> 4. (conv conv pool) * 4 (dense) * 2       
  
 # 20180827 : YOLO 설치 및 예제 실습   
 - YOLO 설치   
 > Image Detection with YOLO-v2 (https://www.youtube.com/watch?v=PyjBd7IDYZs)   
   
 # 20180828 : Custom Object Detection with YOLO   
 - step 500 까지 학습을 진행한 결과   
 ![yolo_test1](https://user-images.githubusercontent.com/41510487/44968622-e279a680-af83-11e8-9c6f-07183d512ae9.jpg)   
 ![yolo_test2](https://user-images.githubusercontent.com/41510487/44968641-f91ffd80-af83-11e8-9204-4dd0d31c4138.jpg)     
    
 # 20180917 : YOLO 개발환경 점검   
 - 설치파일 목록   
 > python36   
 > cython   
 > opencv   
 > tensorflow-gpu   
 > keras   
 > numpy   
 > CUDA9.0   
 > cuDNN v7.2.1   
 > pycharm (Anaconda)   
 > YOLO weight, cfg   
 > darknet   
 > darkflow   
 
 # 20181001 : YOLO 학습 
 - CUDA 설치 시 visual studio integration 실패
 
 # 20181003 : YOLO 학습
 - 성능 좋은 GPU를 사용하기 위해 퍼플 피시방에서 YOLO 설치 시도 - C드라이브 용량 부족으로 실패
 
 # 20181105 : YOLO 학습
 - 아산공학관 125-2호에서 CUDA 설치 실패
 - 아산공학관 223호에서 GPU(NVIDIA GeForce GT 625)있는 컴퓨터 한 대, GPU 없는 컴퓨터 두 대 이용해 YOLO 학습 진행
 
 # 20181107 : webcam 테스트
 - 1812개의 dataset을 이용해 step 7000 까지 학습을 진행한 결과
 - (사진)
 
 # 20181112 : dataset 추가
 - 새로 촬영한 사진과 사진들의 flip본을 이용하여 dataset을 6151개로 늘림
 
 # 20181114 : YOLO 학습
 - 6151개의 dataset을 이용해 YOLO 학습 진행
 
 # 20181118 : webcam 테스트
 - 6151개의 dataset을 이용해 step 42000 까지 학습을 진행한 결과
 - (사진)
 
 # 20181120 : dataset 추가
 - 3952개의 dataset을 추가함
 
