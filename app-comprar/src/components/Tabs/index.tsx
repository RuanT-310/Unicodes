import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { styles } from './styles';

interface Props {
  filter: 'pending' | 'completed';
  onSelectFilter: (filter: 'pending' | 'completed') => void;
  onClear: () => void;
}

export const Tabs: React.FC<Props> = ({ filter, onSelectFilter, onClear }) => {
  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={() => onSelectFilter('pending')} style={styles.tabButton}>
        <Text style={[styles.tabText, filter === 'pending' && styles.tabTextActive]}>
          Pendentes
        </Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => onSelectFilter('completed')} style={styles.tabButton}>
        <Text style={[styles.tabText, filter === 'completed' && styles.tabTextActive]}>
          Comprados
        </Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={onClear} style={styles.clearButton}>
        <Text style={styles.clearText}>Limpar</Text>
      </TouchableOpacity>
    </View>
  );
};