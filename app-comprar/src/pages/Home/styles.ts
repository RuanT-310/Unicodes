import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#D0D2D8',
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 100,
    gap: 20
  },
  logo: {
    top: -25,
    width: 134,
    height: 34,
  },
  listContainer: {
    flex: 1, // ESTE É O IMPORTANTE! Faz o contêiner da lista ocupar todo o espaço restante.
    backgroundColor: '#FFFFFF',
    borderTopLeftRadius: 30,
    borderTopRightRadius: 30,
    paddingHorizontal: 20,
    paddingTop: 20,
    width: '100%',
    
  },
  hrLine: {
    borderBottomColor: '#444444ff', // Or any color you prefer
    borderBottomWidth: StyleSheet.hairlineWidth, // Creates a very thin line
    marginTop: 10
    // You can also use a fixed number for borderBottomWidth like 1
    // marginVertical: 10, // Optional: Add vertical spacing
  }
});
