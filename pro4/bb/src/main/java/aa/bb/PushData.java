package aa.bb;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.Callable;

import org.web3j.abi.FunctionEncoder;
import org.web3j.abi.TypeReference;
import org.web3j.abi.datatypes.Function;
import org.web3j.abi.datatypes.Type;
import org.web3j.abi.datatypes.Utf8String;
import org.web3j.crypto.Credentials;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.RemoteCall;
import org.web3j.protocol.core.methods.request.Transaction;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.tuples.generated.Tuple2;
import org.web3j.tx.Contract;
import org.web3j.tx.TransactionManager;

/**
 * <p>Auto generated code.
 * <p><strong>Do not modify!</strong>
 * <p>Please use the <a href="https://docs.web3j.io/command_line.html">web3j command line tools</a>,
 * or the org.web3j.codegen.SolidityFunctionWrapperGenerator in the 
 * <a href="https://github.com/web3j/web3j/tree/master/codegen">codegen module</a> to update.
 *
 * <p>Generated with web3j version 3.2.0.
 */
public class PushData extends Contract {
    private static final String BINARY = null;

    protected static final HashMap<String, String> _addresses;

    static {
        _addresses = new HashMap<>();
    }

    protected PushData(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    protected PushData(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    public RemoteCall<Tuple2<String, String>> getTable(String databaseName, String tableName) {
        final Function function = new Function("getTable", 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}, new TypeReference<Utf8String>() {}));
        return new RemoteCall<Tuple2<String, String>>(
                new Callable<Tuple2<String, String>>() {
                    @Override
                    public Tuple2<String, String> call() throws Exception {
                        List<Type> results = executeCallMultipleValueReturn(function);;
                        return new Tuple2<String, String>(
                                (String) results.get(0).getValue(), 
                                (String) results.get(1).getValue());
                    }
                });
    }

    public RemoteCall<TransactionReceipt> addTable(String databaseName, String tableName, String keys, String values) {
        Function function = new Function(
                "addTable", 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName), 
                new org.web3j.abi.datatypes.Utf8String(keys), 
                new org.web3j.abi.datatypes.Utf8String(values)), 
                Collections.<TypeReference<?>>emptyList());
//        		String encodedFunction = FunctionEncoder.encode(function);
//        		Transaction transaction = Transaction.createFunctionCallTransaction(
//	             , <gasPrice>, <gasLimit>, contractAddress, <funds>, encodedFunction);
//
//	org.web3j.protocol.core.methods.response.EthSendTransaction transactionResponse =
//	             web3j.ethSendTransaction(transaction).sendAsync().get();

	//String transactionHash = transactionResponse.getTransactionHash();
//
        return executeRemoteCallTransaction(function);
    }

    public RemoteCall<TransactionReceipt> existSuchDatabase(String databaseName) {
        Function function = new Function(
                "existSuchDatabase", 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public static RemoteCall<PushData> deploy(Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(PushData.class, web3j, credentials, gasPrice, gasLimit, BINARY, "");
    }

    public static RemoteCall<PushData> deploy(Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(PushData.class, web3j, transactionManager, gasPrice, gasLimit, BINARY, "");
    }

    public static PushData load(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return new PushData(contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    public static PushData load(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return new PushData(contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    protected String getStaticDeployedAddress(String networkId) {
        return _addresses.get(networkId);
    }

    public static String getPreviouslyDeployedAddress(String networkId) {
        return _addresses.get(networkId);
    }
}
