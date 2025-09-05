import { StatusBar } from 'expo-status-bar';
import { Text, View } from 'react-native';
import { styles } from "./styles"
import { Button } from '@/components/Button';
import { Logo } from '@/components/Logo';
import { Input } from '@/components/Input';
import { useState } from 'react';

export function Home() {
    const [text, setText] = useState('');

    const handlePress = () => {
        if (text.trim()) {
        //onAddItem(text);
        setText('');
        }
    };
  return (
    <View style={styles.container}>
        <Logo style={styles.logo}/>
        <Input 
        placeholder='O que você precisa comprar?'
        value={text}
        onChangeText={setText}
        />
        <Button title='Adicionar' onPress={handlePress}/>
      <StatusBar style="auto" />
    </View>
  );
}