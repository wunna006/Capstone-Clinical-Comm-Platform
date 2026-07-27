import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, SafeAreaView, TouchableOpacity, Switch, Alert, ScrollView } from 'react-native';

export default function App() {
  const [isConsentGranted, setIsConsentGranted] = useState(false);
  
  useEffect(() => {
    // Connect to the Python WebSocket
    const ws = new WebSocket('ws://192.168.1.3:8000/ws/alerts');

    ws.onmessage = (e) => {
      const newAlert = JSON.parse(e.data);
      // Add new alert to the top of the list
      setCriticalAlerts(prev => [newAlert, ...prev]);
      
      // Optional: Trigger a local notification or sound to bypass silent mode
      console.log("Critical Event Received:", newAlert.event);
    };

    ws.onerror = (e) => console.error("WebSocket Error:", e.message);
    
    return () => ws.close(); // Cleanup on unmount
  }, []);

  // Mock data for real-time telemetry events
  const [criticalAlerts, setCriticalAlerts] = useState([
    { id: '1', room: 'ICU-4', event: 'O2 Saturation < 85%', time: '2m ago' },
    { id: '2', room: 'ICU-2', event: 'Bradycardia Detected', time: '5m ago' }
  ]);

  const toggleConsent = () => setIsConsentGranted(previousState => !previousState);

  const handleStartAI = () => {
    if (!isConsentGranted) {
      Alert.alert("Consent Required", "Confirm patient consent before starting recording.");
      return;
    }
    Alert.alert("Ambient AI", "Recording started...");
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.header}>
          <Text style={styles.title}>Clinical Platform</Text>
          <Text style={styles.status}>System Status: Online</Text>
        </View>

        {/* NEW: Critical Alerts Section */}
        <View style={styles.alertSection}>
          <Text style={styles.sectionLabel}>CRITICAL ALERTS</Text>
          {criticalAlerts.map(alert => (
            <View key={alert.id} style={styles.alertBanner}>
              <View style={styles.alertInfo}>
                <Text style={styles.alertRoom}>{alert.room}</Text>
                <Text style={styles.alertEvent}>{alert.event}</Text>
              </View>
              <Text style={styles.alertTime}>{alert.time}</Text>
            </View>
          ))}
        </View>

        <View style={styles.dashboard}>
          <TouchableOpacity style={styles.card} onPress={() => Alert.alert('Messages', 'Opening chat...')}>
            <Text style={styles.cardTitle}>Secure Messaging</Text>
            <Text style={styles.cardDesc}>Two-way encrypted communication.</Text>
          </TouchableOpacity>

          <View style={[styles.card, styles.aiCard]}>
            <Text style={styles.cardTitle}>Ambient AI Transcription</Text>
            <View style={styles.consentRow}>
              <Text style={styles.consentText}>Patient Consent Obtained</Text>
              <Switch
                trackColor={{ false: "#767577", true: "#4CAF50" }}
                onValueChange={toggleConsent}
                value={isConsentGranted}
              />
            </View>
            <TouchableOpacity 
              style={[styles.actionButton, !isConsentGranted && styles.disabledButton]} 
              onPress={handleStartAI}
            >
              <Text style={styles.buttonText}>Start Recording</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#121212' },
  scrollContent: { padding: 20 },
  header: { marginTop: 30, marginBottom: 20, alignItems: 'center' },
  title: { color: '#FFFFFF', fontSize: 28, fontWeight: 'bold' },
  status: { color: '#4CAF50', fontSize: 16 },
  
  // Alert Section Styles
  alertSection: { marginBottom: 25 },
  sectionLabel: { color: '#FF5252', fontWeight: 'bold', fontSize: 12, letterSpacing: 1, marginBottom: 10 },
  alertBanner: { 
    backgroundColor: '#331010', 
    padding: 15, 
    borderRadius: 8, 
    flexDirection: 'row', 
    justifyContent: 'space-between', 
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#FF5252',
    marginBottom: 10
  },
  alertRoom: { color: '#FF5252', fontWeight: 'bold', fontSize: 16 },
  alertEvent: { color: '#FFFFFF', fontSize: 14 },
  alertTime: { color: '#FF5252', fontSize: 12 },

  dashboard: { gap: 20 },
  card: { backgroundColor: '#1E1E1E', padding: 20, borderRadius: 12, borderLeftWidth: 5, borderLeftColor: '#2196F3' },
  aiCard: { borderLeftColor: '#9C27B0' },
  cardTitle: { color: '#FFFFFF', fontSize: 18, fontWeight: 'bold' },
  cardDesc: { color: '#BBBBBB', fontSize: 14, marginTop: 5 },
  consentRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginVertical: 15, padding: 10, backgroundColor: '#2A2A2E', borderRadius: 8 },
  consentText: { color: '#FFFFFF', fontSize: 14 },
  actionButton: { backgroundColor: '#9C27B0', padding: 12, borderRadius: 8, alignItems: 'center' },
  disabledButton: { backgroundColor: '#4A4A4A' },
  buttonText: { color: '#FFFFFF', fontWeight: 'bold' }
});