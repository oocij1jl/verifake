import React from 'react';
import { View, Text, SafeAreaView, TouchableOpacity, StyleSheet, ScrollView } from 'react-native';

export const HomeScreen = ({ navigation }: any) => {
  return (
    <SafeAreaView style={styles.container}>
      {/* 헤더 */}
      <View style={styles.header}>
        <Text style={styles.logo}>VeriFake</Text>
      </View>

      <ScrollView contentContainerStyle={styles.body}>
        {/* 서비스 소개(최근 기록 대신1) */}
        <View style={styles.introSection}>
          <Text style={styles.mainTitle}>조작된 영상으로부터{"\n"}진실을 확인하세요</Text>
          <Text style={styles.subTitle}>
            AI 기반 딥페이크 탐지 기술로 영상의 진위 여부와{"\n"}자연어 기반의 상세한 분석 근거를 제공합니다.
          </Text>
        </View>

        {/* 액션 버튼 */}
        <TouchableOpacity
          style={styles.mainBtn}
          onPress={() => navigation.navigate('DetectionInput')}
        >
          <View style={styles.btnContent}>
            <Text style={styles.btnIcon}>▶</Text>
            <Text style={styles.btnText}>새로운 영상 탐지 시작</Text>
          </View>
        </TouchableOpacity>

        {/* 가이드(최근 기록 대신2) */}
        <View style={styles.guideCard}>
          <Text style={styles.guideLabel}>TIP</Text>
          <Text style={styles.guideText}>
            SNS에서 확인하고 싶은 영상을{"\n"}
            '공유하기' 버튼을 통해 바로 분석할 수 있습니다.
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0a0a0f' },
  header: { paddingHorizontal: 20, paddingVertical: 16 },
  logo: { color: '#7c6cfa', fontSize: 20, fontWeight: 'bold' },
  body: { paddingHorizontal: 20, paddingTop: 40 },

  introSection: { marginBottom: 48 },
  mainTitle: { color: '#fff', fontSize: 28, fontWeight: 'bold', lineHeight: 38 },
  subTitle: { color: '#444468', fontSize: 15, marginTop: 12, lineHeight: 22 },

  mainBtn: {
    backgroundColor: '#7c6cfa',
    borderRadius: 20,
    paddingVertical: 24,
    alignItems: 'center',
    shadowColor: '#7c6cfa',
    shadowOpacity: 0.5,
    shadowRadius: 15,
    elevation: 8
  },
  btnContent: { flexDirection: 'row', alignItems: 'center' },
  btnIcon: { color: '#fff', fontSize: 18, marginRight: 10 },
  btnText: { color: '#fff', fontSize: 18, fontWeight: 'bold' },

  guideCard: {
    marginTop: 40,
    backgroundColor: '#161622',
    padding: 20,
    borderRadius: 16,
    borderLeftWidth: 4,
    borderLeftColor: '#7c6cfa'
  },
  guideLabel: { color: '#7c6cfa', fontSize: 12, fontWeight: 'bold', marginBottom: 8 },
  guideText: { color: '#e1e1e6', fontSize: 14, lineHeight: 20 }
});