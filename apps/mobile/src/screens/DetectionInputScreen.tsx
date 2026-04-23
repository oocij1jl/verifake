import React, { useState } from 'react';
import { View, Text, SafeAreaView, TouchableOpacity, TextInput } from 'react-native';
import { CloudArrowUpIcon, LinkIcon } from 'react-native-heroicons/outline';
import { styles } from './DetectionScreen.styles';
import { BottomNavigation } from '../components/BottomNavigaton';

export const DetectionInputScreen = ({ navigation }: any) => {
    const [url, setUrl] = useState('');

    // 분석 시작 버튼 클릭 시 분석 중 화면으로 이동
    const handleStartAnalysis = () => {
        navigation.navigate('Analysis');
    };

    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>새로운 탐지 시작</Text>
                <Text style={styles.subTitle}>분석할 영상 파일이나 링크를 등록해주세요</Text>

                {/* 파일 업로드 */}
                <TouchableOpacity style={styles.uploadBox} onPress={handleStartAnalysis}>
                    <CloudArrowUpIcon size={48} color="#7c6cfa" strokeWidth={1.5} />
                    <Text style={styles.uploadText}>파일을 드래그하거나 선택하세요</Text>
                    <Text style={styles.uploadSubText}>MP4, MOV, AVI (최대 100MB)</Text>
                </TouchableOpacity>

                <View style={styles.divider}>
                    <View style={styles.line} />
                    <Text style={styles.dividerText}>또는</Text>
                    <View style={styles.line} />
                </View>

                {/* URL 입력 */}
                <View style={styles.inputContainer}>
                    <LinkIcon size={20} color="#444468" style={styles.inputIcon} />
                    <TextInput
                        style={styles.input}
                        placeholder="영상 URL 주소를 붙여넣으세요"
                        placeholderTextColor="#444468"
                        value={url}
                        onChangeText={setUrl}
                    />
                </View>

                {/* 분석 버튼 */}
                <TouchableOpacity
                    style={[styles.startBtn, !url && { opacity: 0.8 }]}
                    onPress={handleStartAnalysis}
                >
                    <Text style={styles.startBtnText}>영상 분석 시작하기</Text>
                </TouchableOpacity>
            </View>

            <BottomNavigation activeRoute="DetectionInput" />
        </SafeAreaView>
    );
};