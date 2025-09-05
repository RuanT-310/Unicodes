import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';
import { styles } from './styles';
import { HrLine } from '../HrLine';
import { ShoppingItem } from '@/interfaces/shopping-item';
interface Props {
  item: ShoppingItem;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}
export const ListItem: React.FC<Props> = ({ item, onToggle, onDelete }) => {
  return (<>
    <View style={styles.container}>
      <View style={styles.pressContent}>
        <TouchableOpacity onPress={() => onToggle(item.id)}>
          {item.isCompleted ? (
            <Icon name="check-circle" size={20} color="#2C46B1" />
          ) : (
            <Icon name="circle" size={20} color="#1E1E1E" />
          )}
        </TouchableOpacity>
        <Text>
          {item.text}
        </Text>
      </View>
      <TouchableOpacity onPress={() => onDelete(item.id)} >
        <Icon name="trash-2" size={20} color="#828282" />
      </TouchableOpacity>
    </View>
    <HrLine marginTop={1}/>
    </>
  );
};