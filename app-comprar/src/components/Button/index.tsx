import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { styles } from './style';

export const Button = ({ title, onPress, disabled }: {title: string, onPress: (e: any) => void, disabled: boolean}) => {
  return (
    <TouchableOpacity style={styles.button} onPress={onPress} disabled={disabled}>
      <Text style={styles.buttonText}>{title}</Text>
    </TouchableOpacity>
  );
};