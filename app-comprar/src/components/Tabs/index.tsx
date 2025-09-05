import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { styles } from './styles';
import Icon from 'react-native-vector-icons/Feather';

interface Props {
  filter: 'pending' | 'completed';
  onSelectFilter: (filter: 'pending' | 'completed') => void;
  onClear: () => void;
}

export const Tabs: React.FC<Props> = ({ filter, onSelectFilter, onClear }) => {
  return (
    <View style={styles.container}>
      <View style={styles.tabs}>
        <TouchableOpacity onPress={() => onSelectFilter('pending')} style={styles.tabButton}>
          <Icon name='circle' size={15} color={filter === 'pending' ? styles.tabTextActive.color : styles.tabText.color}/>
          <Text style={[styles.tabText, filter === 'pending' && styles.tabTextActive]}>
            Pendentes
          </Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => onSelectFilter('completed')} style={styles.tabButton}>
          <Icon name='check-circle' size={15} color={filter === 'completed' ? "#2C46B1" : styles.tabText.color}/>
          <Text style={[styles.tabText, filter === 'completed' && styles.tabTextActive]}>
            Comprados
          </Text>
        </TouchableOpacity>
      </View>
      <TouchableOpacity onPress={onClear}>
        <Text style={styles.tabText}>Limpar</Text>
      </TouchableOpacity>
    </View>
  );
};