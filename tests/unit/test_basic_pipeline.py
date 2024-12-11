from typing import TYPE_CHECKING
import pytest
from src.pipelines.assets.basic_pipeline import raw_sales_data, processed_sales_data

if TYPE_CHECKING:
    from pytest_mock import MockerFixture
    from dagster import AssetExecutionContext

def test_raw_sales_data(mocker: "MockerFixture") -> None:
    """
    Test the raw_sales_data asset function.
    
    Args:
        mocker: Pytest mocker fixture.
    """
    # Mock the context
    mock_context = mocker.Mock(spec=AssetExecutionContext)
    mock_context.log = mocker.Mock()
    
    # Execute the asset
    result = raw_sales_data(mock_context)
    
    # Assertions
    assert len(result) == 3
    assert list(result.columns) == ['date', 'product_id', 'quantity', 'price']
    mock_context.log.info.assert_called_once()

def test_processed_sales_data(mocker: "MockerFixture") -> None:
    """
    Test the processed_sales_data asset function.
    
    Args:
        mocker: Pytest mocker fixture.
    """
    # Mock the context
    mock_context = mocker.Mock(spec=AssetExecutionContext)
    mock_context.log = mocker.Mock()
    
    # Create test input data
    raw_data = raw_sales_data(mock_context)
    
    # Execute the asset
    result = processed_sales_data(mock_context, raw_data)
    
    # Assertions
    assert isinstance(result, dict)
    assert 'dates' in result
    assert 'revenues' in result
    assert len(result['dates']) == len(result['revenues'])
    mock_context.log.info.assert_called_once() 