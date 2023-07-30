# 너의 평점은

'''
전공평점을 계산해주는 프로그램
전공평점은 전공과목별 (학점 * 과목평점)의 합을 학점의 총합으로 나눈 값
등급에 따른 과목평점
A+	4.5
A0	4.0
B+	3.5
B0	3.0
C+	2.5
C0	2.0
D+	1.5
D0	1.0
F	0.0

P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외

입력
20줄에 걸쳐 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분
출력
전공평점을 출력

제한
- 1 ≤ 과목명의 길이 ≤ 50
- 과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
- 학점은 1.0,2.0,3.0,4.0중 하나이다.
- 등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
- 적어도 한 과목은 등급이 P가 아님이 보장된다.

예제 입력1
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P

예제 출력1
3.284483


예제 입력2
BruteForce 3.0 F
Greedy 1.0 F
DivideandConquer 2.0 F
DynamicProgramming 3.0 F
DepthFirstSearch 4.0 F
BreadthFirstSearch 3.0 F
ShortestPath 4.0 F
DisjointSet 2.0 F
MinimumSpanningTree 2.0 F
TopologicalSorting 1.0 F
LeastCommonAncestor 2.0 F
SegmentTree 4.0 F
EulerTourTechnique 3.0 F
StronglyConnectedComponent 2.0 F
BipartiteMatching 2.0 F
MaximumFlowProblem 3.0 F
SuffixArray 1.0 F
HeavyLightDecomposition 4.0 F
CentroidDecomposition 3.0 F
SplayTree 1.0 F

예제 출력2
0.000000
'''

subject_grade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
}

CREDIT = 1
SUBJECT_GRADE = 2
total_credit = 0.0
total_grade = 0.0

for num in range(20):
    score = input().split()
    if score[SUBJECT_GRADE] == 'P':
        continue
    total_credit += float(score[CREDIT])
    total_grade += float(score[CREDIT]) * subject_grade[score[SUBJECT_GRADE]]

print(total_grade/total_credit)


# input = list(input().split())