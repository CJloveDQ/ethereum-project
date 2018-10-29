package push;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import org.web3j.abi.EventEncoder;
import org.web3j.abi.TypeReference;
import org.web3j.abi.datatypes.Bool;
import org.web3j.abi.datatypes.Event;
import org.web3j.abi.datatypes.Function;
import org.web3j.abi.datatypes.Type;
import org.web3j.abi.datatypes.Utf8String;
import org.web3j.abi.datatypes.generated.Uint256;
import org.web3j.crypto.Credentials;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.DefaultBlockParameter;
import org.web3j.protocol.core.RemoteCall;
import org.web3j.protocol.core.methods.request.EthFilter;
import org.web3j.protocol.core.methods.response.Log;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.tx.Contract;
import org.web3j.tx.TransactionManager;
import org.web3j.tx.gas.ContractGasProvider;
import rx.Observable;
import rx.functions.Func1;

/**
 * <p>Auto generated code.
 * <p><strong>Do not modify!</strong>
 * <p>Please use the <a href="https://docs.web3j.io/command_line.html">web3j command line tools</a>,
 * or the org.web3j.codegen.SolidityFunctionWrapperGenerator in the 
 * <a href="https://github.com/web3j/web3j/tree/master/codegen">codegen module</a> to update.
 *
 * <p>Generated with web3j version 3.6.0.
 */
public class PushMes extends Contract {
    private static final String BINARY = "608060405234801561001057600080fd5b50611461806100206000396000f3006080604052600436106100985763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416632e556569811461009d5780633338e509146101a9578063435e7c9b1461025257806356004b6a1461032b57806360773143146104005780636d823690146104995780639b6e11cd146104f2578063e15e51dc14610589578063f0e17ceb146105f6575b600080fd5b3480156100a957600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261013494369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a99988101979196509182019450925082915084018382808284375094975061068d9650505050505050565b6040805160208082528351818301528351919283929083019185019080838360005b8381101561016e578181015183820152602001610156565b50505050905090810190601f16801561019b5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156101b557600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261024094369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a9998810197919650918201945092508291508401838280828437509497506107df9650505050505050565b60408051918252519081900360200190f35b34801561025e57600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261032994369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a99988101979196509182019450925082915084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a99988101979196509182019450925082915084018382808284375094975050933594506108a69350505050565b005b34801561033757600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261032994369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a99988101979196509182019450925082915084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a999881019791965091820194509250829150840183828082843750949750610abf9650505050505050565b34801561040c57600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261013494369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a9998810197919650918201945092508291508401838280828437509497505093359450610df09350505050565b3480156104a557600080fd5b506040805160206004803580820135601f8101849004840285018401909552848452610329943694929360249392840191908190840183828082843750949750610f719650505050505050565b3480156104fe57600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261032994369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a9998810197919650918201945092508291508401838280828437509497506110e99650505050505050565b34801561059557600080fd5b506040805160206004803580820135601f81018490048402850184019095528484526105e29436949293602493928401919081908401838280828437509497506111b79650505050505050565b604080519115158252519081900360200190f35b34801561060257600080fd5b506040805160206004803580820135601f81018490048402850184019095528484526105e294369492936024939284019190819084018382808284375050604080516020601f89358b018035918201839004830284018301909452808352979a9998810197919650918201945092508291508401838280828437509497506112349650505050505050565b60606000836040518082805190602001908083835b602083106106c15780518252601f1990920191602091820191016106a2565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842086519094879450925082918401908083835b6020831061071d5780518252601f1990920191602091820191016106fe565b518151600019602094850361010090810a820192831692199390931691909117909252949092019687526040805197889003820188208054601f60026001831615909802909501169590950492830182900482028801820190528187529294509250508301828280156107d15780601f106107a6576101008083540402835291602001916107d1565b820191906000526020600020905b8154815290600101906020018083116107b457829003601f168201915b505050505090505b92915050565b600080836040518082805190602001908083835b602083106108125780518252601f1990920191602091820191016107f3565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842086519094879450925082918401908083835b6020831061086e5780518252601f19909201916020918201910161084f565b51815160209384036101000a600019018019909216911617905292019485525060405193849003019092206001015495945050505050565b6000846040518082805190602001908083835b602083106108d85780518252601f1990920191602091820191016108b9565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842087519094889450925082918401908083835b602083106109345780518252601f199092019160209182019101610915565b51815160209384036101000a600019018019909216911617905292019485525060408051948590038201852085820190915285855284820187815260019182018054808401808355600092835291859020885160029092020190815591518051919796509194506109ad9392850192919091019061130c565b505050507fd49f44d890ab814a89565fbc00d26005316d650d3eb69d55b23a9539223d6754848483604051808060200180602001848152602001838103835286818151815260200191508051906020019080838360005b83811015610a1c578181015183820152602001610a04565b50505050905090810190601f168015610a495780820380516001836020036101000a031916815260200191505b50838103825285518152855160209182019187019080838360005b83811015610a7c578181015183820152602001610a64565b50505050905090810190601f168015610aa95780820380516001836020036101000a031916815260200191505b509550505050505060405180910390a150505050565b610ac8836111b7565b1515610ad757610ad783610f71565b610ae18383611234565b1515610deb57806000846040518082805190602001908083835b60208310610b1a5780518252601f199092019160209182019101610afb565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842087519094889450925082918401908083835b60208310610b765780518252601f199092019160209182019101610b57565b51815160209384036101000a60001901801990921691161790529201948552506040519384900381019093208451610bb7959194919091019250905061130c565b5060016002846040518082805190602001908083835b60208310610bec5780518252601f199092019160209182019101610bcd565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842087519094889450925082918401908083835b60208310610c485780518252601f199092019160209182019101610c29565b51815160209384036101000a6000190180199092169116179052920194855250604080519485900382018520805460ff191696151596909617909555606080855288519085015287517fd699a90d163a78b510a69d4c72012c9cd72f4f5509cfbf441dfc61baf5d304dd9589958995508894509283928382019284019160808501919089019080838360005b83811015610cec578181015183820152602001610cd4565b50505050905090810190601f168015610d195780820380516001836020036101000a031916815260200191505b50848103835286518152865160209182019188019080838360005b83811015610d4c578181015183820152602001610d34565b50505050905090810190601f168015610d795780820380516001836020036101000a031916815260200191505b50848103825285518152855160209182019187019080838360005b83811015610dac578181015183820152602001610d94565b50505050905090810190601f168015610dd95780820380516001836020036101000a031916815260200191505b50965050505050505060405180910390a15b505050565b60606000846040518082805190602001908083835b60208310610e245780518252601f199092019160209182019101610e05565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842087519094889450925082918401908083835b60208310610e805780518252601f199092019160209182019101610e61565b51815160209384036101000a6000190180199092169116179052920194855250604051938490030190922060010180549092508491508110610ebe57fe5b90600052602060002090600202016001018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610f635780601f10610f3857610100808354040283529160200191610f63565b820191906000526020600020905b815481529060010190602001808311610f4657829003601f168201915b505050505090509392505050565b610f7a816111b7565b15156110e65760206040519081016040526000826040518082805190602001908083835b60208310610fbd5780518252601f199092019160209182019101610f9e565b51815160209384036101000a600019018019909216911617905292019490945260405186516001965086955087945090925082918401908083835b602083106110175780518252601f199092019160209182019101610ff8565b51815160209384036101000a6000190180199092169116179052920194855250604080519485900382018520805460ff19169615159690961790955580845285518482015285517f63fc73ce6a9a5a2357b23927037bc30829d58769fb69c9c5bfef76871b178dd8958795945084935083019185019080838360005b838110156110ab578181015183820152602001611093565b50505050905090810190601f1680156110d85780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b50565b6000826040518082805190602001908083835b6020831061111b5780518252601f1990920191602091820191016110fc565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842085519094869450925082918401908083835b602083106111775780518252601f199092019160209182019101611158565b51815160209384036101000a600019018019909216911617905292019485525060405193849003019092206111b392506001019050600061138a565b5050565b60006001826040518082805190602001908083835b602083106111eb5780518252601f1990920191602091820191016111cc565b51815160209384036101000a600019018019909216911617905292019485525060405193849003019092205460ff1615915061122b90505750600161122f565b5060005b919050565b60006002836040518082805190602001908083835b602083106112685780518252601f199092019160209182019101611249565b51815160209384036101000a6000190180199092169116179052920194855250604051938490038101842086519094879450925082918401908083835b602083106112c45780518252601f1990920191602091820191016112a5565b51815160209384036101000a600019018019909216911617905292019485525060405193849003019092205460ff161591506113049050575060016107d9565b5060006107d9565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061134d57805160ff191683800117855561137a565b8280016001018555821561137a579182015b8281111561137a57825182559160200191906001019061135f565b506113869291506113ab565b5090565b50805460008255600202906000526020600020908101906110e691906113c8565b6113c591905b8082111561138657600081556001016113b1565b90565b6113c591905b808211156113865760008082556113e860018301826113f1565b506002016113ce565b50805460018160011615610100020316600290046000825580601f1061141757506110e6565b601f0160209004906000526020600020908101906110e691906113ab5600a165627a7a72305820555f513efe9ef1def94c63d2feeff096a768e1fad19ac0d5aa01a63d529f27b20029";

    public static final String FUNC_GETTABLEKEYS = "getTableKeys";

    public static final String FUNC_GETTABLELENGTH = "getTableLength";

    public static final String FUNC_PUSHDATA = "pushData";

    public static final String FUNC_CREATETABLE = "createTable";

    public static final String FUNC_GETTABLE = "getTable";

    public static final String FUNC_CREATEDATABASE = "createDatabase";

    public static final String FUNC_DROPTABLE = "dropTable";

    public static final String FUNC_EXISTSUCHDATABASE = "existSuchDatabase";

    public static final String FUNC_EXSITSUCHTABLE = "exsitSuchTable";

    public static final Event CREATEDATABASE_EVENT = new Event("CreateDatabase", 
            Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}));
    ;

    public static final Event CREATETABLE_EVENT = new Event("CreateTable", 
            Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}, new TypeReference<Utf8String>() {}, new TypeReference<Utf8String>() {}));
    ;

    public static final Event PUSHDATA_EVENT = new Event("PushData", 
            Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}, new TypeReference<Utf8String>() {}, new TypeReference<Uint256>() {}));
    ;

    @Deprecated
    protected PushMes(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    protected PushMes(String contractAddress, Web3j web3j, Credentials credentials, ContractGasProvider contractGasProvider) {
        super(BINARY, contractAddress, web3j, credentials, contractGasProvider);
    }

    @Deprecated
    protected PushMes(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    protected PushMes(String contractAddress, Web3j web3j, TransactionManager transactionManager, ContractGasProvider contractGasProvider) {
        super(BINARY, contractAddress, web3j, transactionManager, contractGasProvider);
    }

    public RemoteCall<String> getTableKeys(String databaseName, String tableName) {
        final Function function = new Function(FUNC_GETTABLEKEYS, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}));
        return executeRemoteCallSingleValueReturn(function, String.class);
    }

    public RemoteCall<BigInteger> getTableLength(String databaseName, String tableName) {
        final Function function = new Function(FUNC_GETTABLELENGTH, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Uint256>() {}));
        return executeRemoteCallSingleValueReturn(function, BigInteger.class);
    }

    public RemoteCall<TransactionReceipt> pushData(String databaseName, String tableName, String value, BigInteger index) {
        final Function function = new Function(
                FUNC_PUSHDATA, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName), 
                new org.web3j.abi.datatypes.Utf8String(value), 
                new org.web3j.abi.datatypes.generated.Uint256(index)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteCall<TransactionReceipt> createTable(String databaseName, String tableName, String keys) {
        final Function function = new Function(
                FUNC_CREATETABLE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName), 
                new org.web3j.abi.datatypes.Utf8String(keys)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteCall<String> getTable(String databaseName, String tableName, BigInteger index) {
        final Function function = new Function(FUNC_GETTABLE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName), 
                new org.web3j.abi.datatypes.generated.Uint256(index)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}));
        return executeRemoteCallSingleValueReturn(function, String.class);
    }

    public RemoteCall<TransactionReceipt> createDatabase(String databaseName) {
        final Function function = new Function(
                FUNC_CREATEDATABASE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteCall<TransactionReceipt> dropTable(String databaseName, String tableName) {
        final Function function = new Function(
                FUNC_DROPTABLE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteCall<Boolean> existSuchDatabase(String databaseName) {
        final Function function = new Function(FUNC_EXISTSUCHDATABASE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Bool>() {}));
        return executeRemoteCallSingleValueReturn(function, Boolean.class);
    }

    public RemoteCall<Boolean> exsitSuchTable(String databaseName, String tableName) {
        final Function function = new Function(FUNC_EXSITSUCHTABLE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.Utf8String(databaseName), 
                new org.web3j.abi.datatypes.Utf8String(tableName)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Bool>() {}));
        return executeRemoteCallSingleValueReturn(function, Boolean.class);
    }

    public List<CreateDatabaseEventResponse> getCreateDatabaseEvents(TransactionReceipt transactionReceipt) {
        List<Contract.EventValuesWithLog> valueList = extractEventParametersWithLog(CREATEDATABASE_EVENT, transactionReceipt);
        ArrayList<CreateDatabaseEventResponse> responses = new ArrayList<CreateDatabaseEventResponse>(valueList.size());
        for (Contract.EventValuesWithLog eventValues : valueList) {
            CreateDatabaseEventResponse typedResponse = new CreateDatabaseEventResponse();
            typedResponse.log = eventValues.getLog();
            typedResponse.databaseName = (String) eventValues.getNonIndexedValues().get(0).getValue();
            responses.add(typedResponse);
        }
        return responses;
    }

    public Observable<CreateDatabaseEventResponse> createDatabaseEventObservable(EthFilter filter) {
        return web3j.ethLogObservable(filter).map(new Func1<Log, CreateDatabaseEventResponse>() {
            @Override
            public CreateDatabaseEventResponse call(Log log) {
                Contract.EventValuesWithLog eventValues = extractEventParametersWithLog(CREATEDATABASE_EVENT, log);
                CreateDatabaseEventResponse typedResponse = new CreateDatabaseEventResponse();
                typedResponse.log = log;
                typedResponse.databaseName = (String) eventValues.getNonIndexedValues().get(0).getValue();
                return typedResponse;
            }
        });
    }

    public Observable<CreateDatabaseEventResponse> createDatabaseEventObservable(DefaultBlockParameter startBlock, DefaultBlockParameter endBlock) {
        EthFilter filter = new EthFilter(startBlock, endBlock, getContractAddress());
        filter.addSingleTopic(EventEncoder.encode(CREATEDATABASE_EVENT));
        return createDatabaseEventObservable(filter);
    }

    public List<CreateTableEventResponse> getCreateTableEvents(TransactionReceipt transactionReceipt) {
        List<Contract.EventValuesWithLog> valueList = extractEventParametersWithLog(CREATETABLE_EVENT, transactionReceipt);
        ArrayList<CreateTableEventResponse> responses = new ArrayList<CreateTableEventResponse>(valueList.size());
        for (Contract.EventValuesWithLog eventValues : valueList) {
            CreateTableEventResponse typedResponse = new CreateTableEventResponse();
            typedResponse.log = eventValues.getLog();
            typedResponse.databaseName = (String) eventValues.getNonIndexedValues().get(0).getValue();
            typedResponse.tableName = (String) eventValues.getNonIndexedValues().get(1).getValue();
            typedResponse.keys = (String) eventValues.getNonIndexedValues().get(2).getValue();
            responses.add(typedResponse);
        }
        return responses;
    }

    public Observable<CreateTableEventResponse> createTableEventObservable(EthFilter filter) {
        return web3j.ethLogObservable(filter).map(new Func1<Log, CreateTableEventResponse>() {
            @Override
            public CreateTableEventResponse call(Log log) {
                Contract.EventValuesWithLog eventValues = extractEventParametersWithLog(CREATETABLE_EVENT, log);
                CreateTableEventResponse typedResponse = new CreateTableEventResponse();
                typedResponse.log = log;
                typedResponse.databaseName = (String) eventValues.getNonIndexedValues().get(0).getValue();
                typedResponse.tableName = (String) eventValues.getNonIndexedValues().get(1).getValue();
                typedResponse.keys = (String) eventValues.getNonIndexedValues().get(2).getValue();
                return typedResponse;
            }
        });
    }

    public Observable<CreateTableEventResponse> createTableEventObservable(DefaultBlockParameter startBlock, DefaultBlockParameter endBlock) {
        EthFilter filter = new EthFilter(startBlock, endBlock, getContractAddress());
        filter.addSingleTopic(EventEncoder.encode(CREATETABLE_EVENT));
        return createTableEventObservable(filter);
    }

    public List<PushDataEventResponse> getPushDataEvents(TransactionReceipt transactionReceipt) {
        List<Contract.EventValuesWithLog> valueList = extractEventParametersWithLog(PUSHDATA_EVENT, transactionReceipt);
        ArrayList<PushDataEventResponse> responses = new ArrayList<PushDataEventResponse>(valueList.size());
        for (Contract.EventValuesWithLog eventValues : valueList) {
            PushDataEventResponse typedResponse = new PushDataEventResponse();
            typedResponse.log = eventValues.getLog();
            typedResponse.databaseName = (String) eventValues.getNonIndexedValues().get(0).getValue();
            typedResponse.tableName = (String) eventValues.getNonIndexedValues().get(1).getValue();
            typedResponse.index = (BigInteger) eventValues.getNonIndexedValues().get(2).getValue();
            responses.add(typedResponse);
        }
        return responses;
    }

    public Observable<PushDataEventResponse> pushDataEventObservable(EthFilter filter) {
        return web3j.ethLogObservable(filter).map(new Func1<Log, PushDataEventResponse>() {
            @Override
            public PushDataEventResponse call(Log log) {
                Contract.EventValuesWithLog eventValues = extractEventParametersWithLog(PUSHDATA_EVENT, log);
                PushDataEventResponse typedResponse = new PushDataEventResponse();
                typedResponse.log = log;
                typedResponse.databaseName = (String) eventValues.getNonIndexedValues().get(0).getValue();
                typedResponse.tableName = (String) eventValues.getNonIndexedValues().get(1).getValue();
                typedResponse.index = (BigInteger) eventValues.getNonIndexedValues().get(2).getValue();
                return typedResponse;
            }
        });
    }

    public Observable<PushDataEventResponse> pushDataEventObservable(DefaultBlockParameter startBlock, DefaultBlockParameter endBlock) {
        EthFilter filter = new EthFilter(startBlock, endBlock, getContractAddress());
        filter.addSingleTopic(EventEncoder.encode(PUSHDATA_EVENT));
        return pushDataEventObservable(filter);
    }

    public static RemoteCall<PushMes> deploy(Web3j web3j, Credentials credentials, ContractGasProvider contractGasProvider) {
        return deployRemoteCall(PushMes.class, web3j, credentials, contractGasProvider, BINARY, "");
    }

    @Deprecated
    public static RemoteCall<PushMes> deploy(Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(PushMes.class, web3j, credentials, gasPrice, gasLimit, BINARY, "");
    }

    public static RemoteCall<PushMes> deploy(Web3j web3j, TransactionManager transactionManager, ContractGasProvider contractGasProvider) {
        return deployRemoteCall(PushMes.class, web3j, transactionManager, contractGasProvider, BINARY, "");
    }

    @Deprecated
    public static RemoteCall<PushMes> deploy(Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(PushMes.class, web3j, transactionManager, gasPrice, gasLimit, BINARY, "");
    }

    @Deprecated
    public static PushMes load(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return new PushMes(contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    @Deprecated
    public static PushMes load(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return new PushMes(contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    public static PushMes load(String contractAddress, Web3j web3j, Credentials credentials, ContractGasProvider contractGasProvider) {
        return new PushMes(contractAddress, web3j, credentials, contractGasProvider);
    }

    public static PushMes load(String contractAddress, Web3j web3j, TransactionManager transactionManager, ContractGasProvider contractGasProvider) {
        return new PushMes(contractAddress, web3j, transactionManager, contractGasProvider);
    }

    public static class CreateDatabaseEventResponse {
        public Log log;

        public String databaseName;
    }

    public static class CreateTableEventResponse {
        public Log log;

        public String databaseName;

        public String tableName;

        public String keys;
    }

    public static class PushDataEventResponse {
        public Log log;

        public String databaseName;

        public String tableName;

        public BigInteger index;
    }
}
